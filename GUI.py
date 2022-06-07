from tkinter import *
import tkinter as tk

import openai

window = tk.Tk()
window.geometry('800x800')
text = tk.StringVar()


def submit():
    prompt = """"Ron is a patient and diligent worker and his boss appreciates his work. However, he tend to put off tasks. How will you tell him that in the sandwich method of feedback?

    The sandwich method of feedback: I noticed the calm tone you use when talking to angry customers, and the incredible patience you have to listen to people who talk long, and I appreciate you for that… However when I see that tasks that were supposed to be done today are postponed tomorrow, I'm in trouble because It will be difficult for us to meet the goals set for us by the management… so I would like to check with you how you can help you keep pace, so that our outputs will not be hurt and at the same time you can continue to be attentive and patient to customers, as you know how to do so well… I know how high your work ethic is and how much you care about the work, I am sure we can find a way to bridge everyone's needs in a way that will suit us all.

    Yossi is a student in high school. He  is a diligent and invested student but he is late for classes. How will you tell him that in the sandwich method of feedback?

    The sandwich method of feedback: I know you are very responsible for preparing your lessons, and you put effort into studying the profession… However I noticed that the week was different 3 times and it caused disruption during the lesson, because my and students' attention was distracted and it took me time to get the class back on track… Is there a reason for these delays and how can they be prevented, so that next time we can ensure proper conduct of the lesson and we can also make sure that you do not lose material due to the delays… And since I know how serious and responsible I have no doubt you will find a way to ensure you arrive on time

    Roni is a caring and considerate young girl who knows how to manage her time well. However, her mother says she is really messy. How will she say that to Roni  in the sandwich method of feedback?

    The sandwich method of feedback: I admire the way you manage your time and combine your studies with your social life and all the other activities you have, and balance all these things… At the same time when I see the piles of clothes on the floor in your room and your personal belongings scattered in different corners of the house (The diary in the living room, the football in the kitchen, the coat in the TV corner), I feel angry because I take care of arranging the house most of the time and I look forward to cooperation from all family members… So I ask you to find time to arrange the room and organize your belongings At home and we will live in an atmosphere of mutual consideration… And since I know how caring and considerate you are, I am sure you will find the time necessary for this

    Omer is an excellent employee who can be trusted to do his tasks on time, and he is very organized, but he needs to improve his writing skills. How will you tell him that in the sandwich method of feedback?
    The sandwich method of feedback:"""

    text.set(textbox.get(1.0, "end-1c"))

    response = \
    openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=256, temperature=1, top_p=1,
                             frequency_penalty=0, presence_penalty=0)["choices"][0]["text"]

    textbox.insert(tk.END, response)


enterTextLabel = tk.Label(window, text="Tell me about the person you want to give him a feedback", font=("courier", 18))
enterTextLabel.place(rely=0.1, relx=0.01)
textbox = tk.Text(window, height=10, width=60, font=("courier", 15))
textbox.place(rely=0.2, relx=0.01)
subButton = tk.Button(window, text="OK", font=("courier", 20), command=submit)
subButton.place(rely=0.75, relx=0.01)
window.mainloop()
