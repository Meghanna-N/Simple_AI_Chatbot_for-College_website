import tkinter as tk
from tkinter import messagebox, filedialog
import pyttsx3
import webbrowser
import speech_recognition as sr
import threading

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Adjust the speech rate for smoother delivery
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

stop_audio_flag = False  # Flag to control TTS playback

# College Info Dictionary
college_info = {
    "admission requirements": (
        "The admission requirements include:\n"
        "1. Copy of S.S.L.C / S.S.C (10th) Marks Card.\n"
        "2. Copy of P.U.C (10+2) Marks Card.\n"
        "3. Copy of Transfer Certificate.\n"
        "4. Copy of Migration Certificate for Non-Karnataka Students.\n"
        "5. Proof of permanent residence.\n"
        "6. Relevant caste and income certificates for Karnataka Candidates.\n"
        "7. Visa and Passport for foreign students.\n"
        "Learn more: https://www.cittumkur.org/admissions/"
    ),
    "college address": (
        "Channabasaveshwara Institute of Technology\n"
        "N.H. 206, B.H. Road, Gubbi, Tumkur 572 216\n"
        "Near Bangalore, Karnataka, India.\n"
        "Tel: 0816-4021402 / 403, 9449637043, 8867354168\n"
        "Email: info@cittumkur.org\n"
        "Map: https://maps.app.goo.gl/EViEJeshMXunETvj7"
    ),
    "placement details": (
        "Our highest package: 4 LPA\n"
        "Average package: 7-9 LPA\n"
        "Top recruiters: Wipro, Infosys, CTS, TCS."
    ),
    "about college": (
        "CIT was established in 2001 to provide quality technical education. "
        "The institute is affiliated to Visvesvaraya Technological University, approved by AICTE, and recognized by the Government of Karnataka. "
        "Located in Tumkur, Karnataka, the campus spans 60 acres of lush green land, offering a pleasant atmosphere for students and staff."
    ),
    "available programs": (
        "UG courses: Computer Science, Electrical Engineering, Civil Engineering, and more.\n"
        "PG courses: M.Tech, MBA.\n"
        "For more details, visit: https://www.cittumkur.org/programs/"
    ),
    "tuition fees": (
        "Here are the course and fee details:\n\n"
            "Course                | Fees           | Eligibility\n"
            "-----------------------+-----------------------------+--------\n"
            "BE (7 Courses)       | ₹10.66 Lakhs  | 10+2 with 45% + KEA\n"
            "M.Tech (3 Courses)   | ₹1.51 Lakhs   | Graduate with Karnataka PGCET\n"
            "MBA (1 Course)       | ₹1.28 Lakhs   | Graduate with CAT\n"
    ),
      "Library Details":(
        "The library provides a vast collection of books, journals, and e-resources. \n "
        " Library Hours \n"
        " Mon – Fri : 9.00am – 7.30pm \n "
        " Sat : 9.00am – 3.30pm \n"
        " Sun : Closed \n "
        "For more details, visit: https://www.cittumkur.org/library-resources/"
    ),
        "Contact Details": (
        "CONTACT DETAILS\n\n"
        "FOR INFORMATION ON        |CONTACT PERSON       |DESIGNATION         |EMAIL                     |CONTACT  NUMBER\n"
        "--------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-\n\n"
        "ADMISSIONS               |Mr.GB JyothiGanesh     |Secretary            |gbjg@gmail.com             |+91 816 4021 402\n"
        "ADMISSIONS FOR NORTH EAST |Mr. Bappi Das         |CIT Associate        |mythikona@gmail.com         |+91 9954099366\n"
        "ACADEMIC MATTERS         |Dr. Anil Kumar G      |Dean (Academic)      |anileverywhere@cittumkur.org|+91 81050159518\n"
        "BUSINESS ALLIANCE &      |Dr. C P. Shantala     |Vice Principal       |shantala.cp@cittumkur.org   |08131 – 223818\n"
        "PLACEMENTS               |Mr. Chetan Balaji     |Placement Officer    |placement@cittumkur.org     |08131 – 223818\n"
        "HOSTEL                   |Mr. Kumaraswamy H     |Deputy Chief Warden  |hr@cittumkur.org            |08131 – 223818\n"
        "GENERAL ENQUIRY          |Mrs. Latha             |Executive – Admn. & HR|hr@cittumkur.org            |+91 813 1223 818\n"
    ),
    "hostel": (
        "CIT runs separate hostels for boys & girls. "
        "The boys' hostel is located on-campus, and the girls' hostel is off-campus. "
        "Healthy food, TV, parking, and 24/7 security are available."
    ),
    "cafeteria": (
        "The cafeteria serves nutritious food and provides a relaxing environment for students and staff."
    ),
    "thank you": (
        "Thank you for using the CIT College Chatbot. Have a great day!"
    )
}

# Sample FAQ data
faq_list = [
    "What are the admission requirements?",
    "Where is the college located?",
    "Tell me about placements.",
    "What programs are available?",
    "What are the hostel facilities like?",
    "What scholarships are available?",
    "How do I contact the administration office?",
]

# Handle clickable links in responses
def open_link(url):
    webbrowser.open(url)

# Respond to user input
def respond_to_input(user_input):
    global stop_audio_flag
    user_input = user_input.lower()
    response = "I'm sorry, I don't have information about that. Please ask something else."

    if any(keyword in user_input for keyword in ["tuition", "fees", "cost"]):
        response = college_info["tuition fees"]
    elif any(keyword in user_input.lower() for keyword in ["admission", "requirements", "apply", "documents"]):
        response = college_info["admission requirements"]
    elif any(keyword in user_input.lower() for keyword in ["location", "address"]):
        response = college_info["college address"]
    elif any(keyword in user_input.lower() for keyword in ["programs", "courses", "study", "degree", "branches", "UG", "PG"]):
        response = college_info["available programs"]
    elif any(keyword in user_input.lower() for keyword in ["aid", "scholarship", "loan"]):
        response = college_info["financial aid"]
    elif any(keyword in user_input.lower() for keyword in ["contact", "phone", "email"]):
        response = college_info["Contact Details"]
    elif any(keyword in user_input.lower() for keyword in [ "information", "info","about college","college details"]):
        response = college_info["about college"]
    elif any(keyword in user_input.lower() for keyword in ["Library", "library"]):
        response = college_info["Library Details"]
    elif any(keyword in user_input.lower() for keyword in ["placement", "internship", "job"]):
        response = college_info["placement details"]
    elif any(keyword in user_input.lower() for keyword in ["thank you", "thanks", "see you"]):
        response = college_info["thank you"]
    elif any(keyword in user_input.lower() for keyword in ["hostel", "stay", "rooms"]):
        response = college_info["hostel"]
    elif any(keyword in user_input.lower() for keyword in ["cafeteria", "canteen", "food"]):
        response = college_info["cafeteria"]
    elif user_input.lower() in ["hi", "hello", "hey"] :
        response = "Hello! How can I assist you today?"
    elif user_input.lower() in ["bye", "exit", "goodbye"]:
        response = "Goodbye! Have a great day."
    
    # Display response in chat history
    chat_history.config(state="normal")
    chat_history.insert(tk.END, f"👤 You: {user_input}\n")
    insert_hyperlinked_text("🤖 Chatbot: "+response)
    chat_history.insert(tk.END, "\n\n")
    chat_history.config(state="disabled")
    chat_history.see(tk.END)

    # Play audio and text response together
    threading.Thread(target=play_audio, args=(response,)).start()

# Insert hyperlinked text into chat history
def insert_hyperlinked_text(text):
    words = text.split()
    for word in words:
        if word.startswith("http://") or word.startswith("https://"):
            chat_history.insert(tk.END, word + " ", "link")
            chat_history.tag_bind("link", "<Button-1>", lambda e, url=word: open_link(url))
        else:
            chat_history.insert(tk.END, word + " ")

# Play audio response
def play_audio(response_text):
    global stop_audio_flag
    stop_audio_flag = False  # Reset stop flag
    engine.say(response_text)
    engine.runAndWait()

# Stop audio
def stop_audio():
    global stop_audio_flag
    stop_audio_flag = True
    engine.stop()

# Voice input handling
def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        user_input = recognizer.recognize_google(audio)
        print(f"User said: {user_input}")
        respond_to_input(user_input)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        respond_to_input("Sorry, I did not catch that. Please try again.")
    except sr.RequestError:
        print("Sorry, the speech recognition service is unavailable.")
        respond_to_input("Sorry, there was an error with the voice recognition service.")

# Start voice input in a separate thread
def start_voice_input():
    voice_thread = threading.Thread(target=voice_input)
    voice_thread.daemon = True
    voice_thread.start()

# Save chat history
def save_chat():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            chat_history_text = chat_history.get("1.0", tk.END).strip()
            file.write(chat_history_text)
        messagebox.showinfo("Success", "Chat history saved successfully!")

# Toggle theme
def toggle_theme():
    if root.cget("bg") == "white":
        root.configure(bg="#2c2c2c")
        chat_frame.configure(bg="#444")
        chat_history.configure(bg="#333", fg="white")
        theme_button.configure(text="Switch to Light Theme")
    else:
        root.configure(bg="white")
        chat_frame.configure(bg="white")
        chat_history.configure(bg="white", fg="black")
        theme_button.configure(text="Switch to Dark Theme")

# Show FAQs in a popup
def show_faq():
    faq_window = tk.Toplevel(root)
    faq_window.title("FAQs")
    faq_window.geometry("400x300")
    faq_window.configure(bg="lightblue")

    def use_faq(faq):
        
        user_entry.delete(0, tk.END)
        user_entry.insert(0, faq)
        respond_to_input(faq)
        faq_window.destroy()

    for faq in faq_list:
        btn = tk.Button(faq_window, text=faq, command=lambda q=faq: use_faq(q), font=("Arial", 12), bg="#4CAF50", fg="white")
        btn.pack(pady=5, fill="x")

# About and Help
def show_about():
    """Display information about the chatbot."""
    messagebox.showinfo("About", "College Chatbot\nVersion 1.0\nDeveloped by Meghana.")

def show_help():
    """Display help dialog."""
    messagebox.showinfo("Help", "Type your query in the input box or use the voice input button.")


# Main GUI
root = tk.Tk()
root.title("CIT College Chatbot")
root.geometry("600x600")
root.configure(bg="#F8F9FA")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Help", command=show_help)

header_label = tk.Label(root, text="CIT College Chatbot", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white")
header_label.pack(fill="x", pady=10)

chat_frame = tk.Frame(root, bg="white")
chat_frame.pack(pady=10, padx=10, fill="both", expand=True)
chat_history = tk.Text(chat_frame, state="disabled", wrap="word", font=("Arial", 12))
chat_history.tag_configure("link", foreground="blue", underline=True)
chat_history.pack(fill="both", expand=True)

user_entry = tk.Entry(root, font=("Arial", 14))
user_entry.pack(padx=10, pady=10, fill="x")
user_entry.bind('<Return>', lambda event: respond_to_input(user_entry.get()))

button_frame = tk.Frame(root, bg="#F8F9FA")
button_frame.pack(pady=10)

send_button = tk.Button(button_frame, text="Send", command=lambda: respond_to_input(user_entry.get()), bg="#4CAF50", fg="white")
send_button.grid(row=0, column=0, padx=5)

voice_button = tk.Button(button_frame, text="🎤 Voice Input", command=voice_input, bg="#2196F3", fg="white")
voice_button.grid(row=0, column=1, padx=5)

stop_button = tk.Button(button_frame, text="⏹ Stop Audio", command=stop_audio, bg="#FF5722", fg="white")
stop_button.grid(row=0, column=2, padx=5)

save_button = tk.Button(button_frame, text="💾 Save Chat", command=save_chat, bg="#4CAF50", fg="white")
save_button.grid(row=0, column=3, padx=5)

theme_button = tk.Button(button_frame, text="Switch to Dark Theme", command=toggle_theme, bg="#FF5733", fg="white")
theme_button.grid(row=0, column=4, padx=5)

faq_button = tk.Button(button_frame, text="📚 FAQs", command=show_faq, bg="#2196F3", fg="white")
faq_button.grid(row=0, column=5, padx=5)

# Run the GUI
root.mainloop()
