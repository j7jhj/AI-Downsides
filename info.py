
import os
import time
def printt(string, strDelay):
  for i in str(string + "\n"):
    print(i, end="", flush=True)
    time.sleep(strDelay)

text = """AI has been around for long enough for us to identify some of the benefits of its use but also it's downsides. A variety of companies use AI 
for things such as online security, however, according to Retail Touchpoints, the use of AI for cyber security has been noted by experts to be connected
to almost 75 percent of cyber attacks. This could be a significant issue for the internet as it confirms that the use of AI for internet security
is unreliable and can lead to negative results such as data leaks, phishing, and privacy concerns.Many people tend to believe that AI's main problem 
is the singularity which is described as an event where technology, including ai, becomes uncontrollable and irreversible that can be unpredictable 
to determine it's effect on human society. However, AI can have a significant impact on the environment as said by Sasha Luccioni who states that the energy
used for AI proccessing is way too demanding and can lead to a increase in global warming due to more energy being needed to run the AI. AI can be also be a
huge concern for workers. According to Wach, K. et al., "By 2030, it is projected that around 375 million individuals (equivalent to 14 percent of the global work-
force) may have to switch professions due to technological advancements related to AI". With this data, it can be asserted that AI can have a negative effect on 
the common workforce, leaving many people without jobs and or having to change occupations to survive finacially.  """

data = """(Retail Touchpoints) Nearly 75 percent seen a increase of cyberattacks and 85 percent claim its AI. This assumes that cyberattacks are more likely to happen
due to AI
          (Wach K. et al.) By 2030 there could be 375 million individuals that have to switch professions due to technoligcal advancement
          
          """

def main_info():
    os.system('clear')
    printt(text, 0.07)
    exit = input("[Type 'exit' to exit]").lower()

    match exit:
        case "exit":
            Info = False
            Loop = True
