# system_msg = "You will be provided with a text, and your task is to classify its sentiment as positive, neutral, or negative and give the topic for it in single line also give the conclusion in three to four line."





# system_msg = """I will give you some text which contains the timely conversation about the video. 
#                           for example:
#                                '0:00:00----> 0:00:02.100000
#                                 Well, let's focus on ITC.'
                                
#                                 here in this example from 0sec to 2.1 second they have talk  'Well, let's focus on ITC.'
                                 
#                             So give me the context what has talked text till 8 seconds  """
                            

system_msg = """
                You will be provided video trasnscript with time frame and conversations happened for that time frame, 
                and your task is to classify its sentiment as positive, neutral, or negative and give the 
                topic for it in single line also give the conclusion in three to four line.
                
                and also give the summary. for summary you need to give the topic name for each time frame discussion.
                for example:
                '0:00:00----> 0:00:02.100000
                Well, let's focus on ITC.'
                
                so you need to give the topic for above discussion like wise give the short topic name for each time frame.
                
                so please remenber your task you need provide below main four information.
                1. Topic: Topic name for overall conversation.
                2. Sentiment: Sentiment for overall conversation.
                3. Conclusion: Conclusion for overall conversation.
                4. Summary: In summary give Topic name for each time frame as explained above.
    
                """                            
                            





