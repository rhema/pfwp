## This file includes functions for drawing text art characters with and messages.
##
##

bubble_text ='''
   =====================
(                        )
   MESSAGE
(                        )
  ====        ==========
    =   ===
   / /
   /
'''

long_cat_start = '''
    ^^
   ( 'w')
    I    ==
    I ==
    I   I\n'''
long_cat_belly = "    I   I\n"
long_cat_end = '''    I   I
=(    I
     I I
'''

def message_in_bubble(message):
    return bubble_text.replace("MESSAGE",message)

def table_guy():
    return table_guy

def long_cat(length=3):
    text = long_cat_start + long_cat_belly*length
    text = text+long_cat_end
    return text