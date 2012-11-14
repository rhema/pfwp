import draw



def test_bubble():
    text = draw.message_in_bubble("You see what I'm saying?")
    print text

def test_long_cat():
    text = draw.message_in_bubble("I am a long cat.")+draw.long_cat()
    print text
    text = draw.message_in_bubble("Not as long as me!")+draw.long_cat(10)
    print text
#test_bubble()
test_long_cat()