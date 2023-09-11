#Python Personal Trainer Chatbot
keywords = ["excercise", "diet", "sleep", "general", "strength", "aerobic"]
responses = ["Excercise helps manage weight, reduces the risk of disease, strengthens bones and muscles, and improves your ability to do everyday activities. There are many different forms of excercise but I can teach you about strength training and Aerobic excercise.","Having a good diet is important in preventing weight gain, heart diesease, diabetes, and cancer. A healthy diet requires eating many fruits and vegetables, lean proteins, healthy fats, carbohydrates, and drinking enough water.","Sleep is essential in having proper brain performance, mood, and health. Sleep is an important part of the muscle building process, for optimal muscle growth you must get a minimum of 7-9 hours of sleep.", "No matter what your fitness goals are whether it be to build muscle, live longer, or have a higher quality of life you must be able to be consistent with your training, diet, and sleep.", "Strength training is the ultilization of intense excercise such as using weights or resistance bands to encourage muscle and/or strength growth.", "Aerobic excercise strengthens your heart and lungs while working the muscles you work during your workout. Aerobic activities include running, cycling, and swimming."]
#Welcome the user
print("Welcome to your very own AI personal trainer!")
#Ask User for name
userName = input("What is your name? ")

#Have chatbot greet user by name
print("Hello " + userName + "!")
print("My advice ranges from excercise, diet, sleep, and general knowlege.")
print("If you no longer require my help just type bye.")
print("What would you like my assistance with?")

user = input("Type your response, or bye to quit: ")
user = user.lower()
while(user != "bye"):
  keyword_found = False
  
  for index in range(len(keywords)):
    if(keywords[index] in user):
      print("Bot: " + responses[index])
      keyword_found = True
      
  if(keyword_found == False):
    print("Sorry, I do not understand your statement. Can you rephrase it for me?")

  user = input("Type your response, or bye to quit: ")
  user=user.lower()