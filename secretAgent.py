'''Code Signal Secret Agents meeting challenge
Nov. 6, 2018'''

def secretAgentsMeetingProposal(incomingMessage, codeNumberDiff):
    shift = 0 #until codeNumberDiff is activated by a "_"
    # The decoding table as a dictionary. Copy and paste these
    # from the instructions. Use "find/replace" to
    # change the equals signs into colons.
    symbols = {"0" : "a",
                "9" : "e",
                "8" : "i",
                "7" : "o",
                "6" : "u",
                "5" : "y",
                "4" : "w",
                "10" : "t",
                "11" : "d",
                "12" : "s",
                "13" : "n",
                "14" : "m",
                "15" : "r",
                "16" : "b",
                "17" : "k",
                "18" : "p",
                "*" : "morning",
                "@" : "afternoon",
                "#" : "night",
                "?" : "-"}
    # This line splits the string at the periods into
    # a list.
    msg = incomingMessage.split('.')
    # Start the output string
    output = ''
    # Go over the message list character by character
    for n in msg:
        if n == "_": # If it's an underline:
            shift += codeNumberDiff #activate the shift number
        elif n in '@#?*': #if it's a special character
            output += symbols[n] #just decode it
        else: # If it's a number, shift it by the shift number,
            # then decode it
            output += symbols[str(int(n) + shift)]
    '''Now output should be in string form:
    today-night-bar
    We'll split it at the dash into a list of
    three values: the day, time and place'''
    output2 = output.split('-')
    day,time,place = output2[0],output2[1],output2[2]
    #print(day)
    #Now check if the day, time and place work for you
    if day == 'today':
        if place != 'park':
            reply = '13.7' #'no'
        else:
            reply = '5.9.12' #'yes'
    elif day == 'tomorrow':
        if (place == 'bar' and time == 'night') or \
           (place == 'park' and time == 'afternoon'):
            reply = '5.9.12' #'yes'
        else:
            reply = '13.7' #'no'
    elif day == 'twodays':
        if place == 'restaurant' and time == 'morning':
            reply = '5.9.12' #'yes'
        else:
            reply = '13.7' #'no'
    return [output,reply]

incomingMessage = "10.4.7.11.0.5._.10.?.*.?._.11.5.8.6.-4.2.11.-4.9.6"

print(secretAgentsMeetingProposal(incomingMessage,2))
