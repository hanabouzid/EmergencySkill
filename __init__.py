# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class EmergencySkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(EmergencySkill, self).__init__(name="EmergencySkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("Emergency"))
    def Emergency(self):
       type= self.get_response('what type of emergency?')
       if  type=='fall':
           self.speak_dialog("Emergency.fall")
       elif type=='fire':
           self.speak_dialog("Emergency.fire")
       elif type =='heart attack':
           rep=self.get_response('is the case conscious? yes or no ?')
           if rep=='yes':
               self.speak_dialog("Emergency.heart.conscious")
           else:
               self.speak_dialog("Emergency.heart.unconscious")
       elif type == 'haemorrhage':
           self.speak_dialog("Emergency.haemorrhage")
       else:
            self.speak("please call 190")

def create_skill():
    return EmergencySkill()
