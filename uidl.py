import PyChromeDevTools
import os
import subprocess
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import PhotoImage
import threading
class ScenarioManager:
    def __init__(self):
        self.scenario_name = ""
        self.scenario_id = ""
        self.url=""
        self.chrome=None
    # Define the directory name

    def extract_all_ids_from_file(self,file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'lxml')
        all_elements = soup.find_all()
        
        element_ids = []
        for element in all_elements:
            element_id = element.get('id')
            if element_id:
                element_ids.append(element_id)
        
        return element_ids

    def find_chrome(self):
        potential_paths = [
            os.path.join(os.getenv('LOCALAPPDATA', ''), r"Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.getenv('PROGRAMFILES', ''), r"Google\\Chrome\\Application\\chrome.exe"),
            os.path.join(os.getenv('PROGRAMFILES(X86)', ''), r"Google\\Chrome\\Application\\chrome.exe"),
        ]
        
        for path in potential_paths:
            if os.path.isfile(path):
                return path
        
        return None

    def get_clicked_element_node_ids(self):
        global outer_html
        result = self.chrome.Runtime.evaluate(expression="window.getClickedElement")
        if result[0]['result']['result']['objectId']:
            objectId_runtime = str(result[0]['result']['result']['objectId'])
            properties = self.chrome.Runtime.getProperties(objectId=objectId_runtime)
            props = properties[0]['result']['result']
            x = next(prop['value']['value'] for prop in props if prop['name'] == 'x')
            y = next(prop['value']['value'] for prop in props if prop['name'] == 'y')
            clicked_node = self.chrome.DOM.getNodeForLocation(x=x, y=y)
            backend_node_id = clicked_node[0]['result']['backendNodeId']
            dom_tree = self.chrome.DOM.getOuterHTML(backendNodeId=backend_node_id)
            dom_tree_dict = dom_tree[0]
            outer_html = dom_tree_dict['result']['outerHTML']
            with open(f"html/{backend_node_id}.html", "w", encoding="utf-8") as file:
                file.write(outer_html)
            return backend_node_id
        return None

    def get_manual_input_value(self):
        result = self.chrome.Runtime.evaluate(expression="window.enteredInputValue")
        entered_input_value = result[0]['result']['result']['value']
        return entered_input_value

    def initialize_bindings(self):
        self.chrome.Runtime.evaluate(expression="""
        document.addEventListener('click', function(event) {
            var x = event.clientX;
            var y = event.clientY;
            window.getClickedElement = { x: x, y: y };
            window.clickHandler(JSON.stringify(window.getClickedElement));
            var element = document.elementFromPoint(x, y);
            if (element) {
                element.style.border = '2px solid red';
            }
        });

        function addInputEventListeners() {
            document.querySelectorAll('input').forEach(input => {
                if (!input.dataset.listenerAdded) {
                    input.dataset.listenerAdded = 'true';
                    input.addEventListener('input', function() {
                        window.enteredInputValue = this.value;
                        window.inputHandler(this.value); // Trigger inputHandler binding
                        this.style.border = '2px solid green';
                        console.log('Input value set:', this.value);
                    });
                }
            });
        }

        addInputEventListeners();

        const observer = new MutationObserver((mutationsList, observer) => {
            for (const mutation of mutationsList) {
                if (mutation.type === 'childList') {
                    mutation.addedNodes.forEach(node => {
                        if (node.tagName === 'INPUT') {
                            addInputEventListeners();
                        } else if (node.querySelectorAll) {
                            node.querySelectorAll('input').forEach(() => {
                                addInputEventListeners();
                            });
                        }
                    });
                }
            }
        });

        observer.observe(document.body, { childList: true, subtree: true });

        window.enteredInputValue = '';
        console.log('Initial event listeners added and MutationObserver set up');
        """)

    def get_scenario_name(self):
        
        # Create the main window
        root = tk.Tk()
        root.geometry("490x490")
        root.title("rRecorder")
        root.configure(bg="#7188B4")
        # Create a label for the title
        title_label = tk.Label(root,text="rRecorder", font=("Helvetica", 18, "bold"),fg="#ffffff",bg="#F06500",relief="solid",bd=0)
        title_label.place(x=180, y=30, width=140, height=50)

        # Create an entry widget for scenario id
        self.url = tk.Entry(root, font=("Arial", 12), width=40, bg="#ACFCB4")
        self.url.place(x=76, y=110)

        #urllabel
        url_label = tk.Label(root, text="Url:", font=("Helvetica",12, "bold"),fg="#000000",bg="#ACFCB4",relief="solid",bd=0)
        url_label.place(x=47, y=111)

        # Create an entry widget for scenario name
        self.scenario_entry = tk.Entry(root, font=("Arial", 12), width=18,bg="#FFD9D9")
        self.scenario_entry.place(x=273, y=150)

        # Create a label for scenario name
        scenario_label = tk.Label(root, text="Scenario Name:", font=("Helvetica",12, "bold"),fg="#000000",bg="#FFD9D9",relief="solid",bd=0)
        scenario_label.place(x=150, y=151)

        # Create an entry widget for scenario id
        self.id_entry = tk.Entry(root, font=("Arial", 12), width=5,bg="#FFD9D9")
        self.id_entry.place(x=83, y=150)

        # Create a label for scenario id
        id_label = tk.Label(root, text="S.Id:", font=("Helvetica",12, "bold"),fg="#000000",bg="#FFD9D9",relief="solid",bd=0)
        id_label.place(x=47, y=151)

        # Create a label for Record, Pause, Stop and Export
        rpse_label=tk.Label(root, bg="#FFFFFF", relief="solid", bd=0)
        rpse_label.place(x=47, y=201, height=60, width=391)

        # Function to get the input and print it
        def get_input():
            self.scenario_name = self.scenario_entry.get()
            self.scenario_id = self.id_entry.get()
            self.url=self.url.get()
            chrome_path = self.find_chrome()
            print(chrome_path)
            if chrome_path:
                try:
                    args = [
                        "--remote-debugging-port=9222",
                        "--remote-allow-origins=*"
                    ]
                    process = subprocess.Popen([chrome_path] + args)
                    self.chrome = PyChromeDevTools.ChromeInterface(port=9222)
                    self.chrome.Network.enable()
                    self.chrome.Page.enable()
                    self.chrome.DOM.enable()
                    self.chrome.Runtime.enable()

                    self.chrome.Page.navigate(url=self.url)
                    self.chrome.wait_event("Page.loadEventFired", timeout=60)

                    # Add bindings for click and input events
                    self.chrome.Runtime.addBinding(name='clickHandler')
                    self.chrome.Runtime.addBinding(name='inputHandler')
                    self.initialize_bindings()
                    inputs = {}

                    def handle_event():
                        self.initialize_bindings()
                        global previous_backend_node_id
                        previous_backend_node_id = None
                        result = self.chrome.wait_event("Runtime.bindingCalled")
                        try:
                            if result and result[0]['params']['name'] == "clickHandler":
                                Action = "Click Button"
                                backend_node_id = self.get_clicked_element_node_ids()
                                if backend_node_id != previous_backend_node_id:
                                    id_for_text = backend_node_id
                                    #previous_backend_node_id = backend_node_id
                                    print(f"Backend Node ID: {backend_node_id}")
                                    file_path = f"html/{backend_node_id}.html"
                                    element_ids = self.extract_all_ids_from_file(file_path)
                                    print(f"The extracted ids are: {element_ids}")
                                    manual_input_value = self.get_manual_input_value()
                                    inputs[id_for_text] = manual_input_value
                                    print(f"Entered Input Value from Click Handler: {manual_input_value}")
                            elif result and result[0]['params']['name'] == "inputHandler":
                                manual_input_value = self.get_manual_input_value()
                                Action = "Enter Text"
                                print(f"Entered Input Value from input handler: {manual_input_value}")
                            print(inputs)
                        except Exception as error:
                            print(error)
                            pass
                        handle_event()
                    event_thread = threading.Thread(target=handle_event,daemon=True)
                    event_thread.start()
                except Exception as error:
                    #print(error)
                    pass
                finally:
                    print("hi")
                    #process.terminate()
                    process.wait()
            else:
                print("Google Chrome not found.")
        # Create a submit button
        submit_button = tk.Button(root, text="Record", command=get_input, font=("Helvetica", 12), bg="red", fg="white",relief="solid",bd=0)
        #submit_button.pack(pady=20)
        submit_button.place(x=82, y=215)
        root.mainloop()
if __name__ == "__main__":
    scenario_manager = ScenarioManager()
    scenario_manager.get_scenario_name()
    scenario_name = scenario_manager.scenario_name
    url= scenario_manager.url            
    print(f"Entered Url :{url}")
    print(f"Scenario Name: {scenario_name}")
    scenario_id = scenario_manager.scenario_id
    print(f"Scenario Id: {scenario_id}")