from constants import *
import logging
import unicodedata
from util.text_format import clean_word, remove_accents

def word_exists(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" is already on the black list.")

def word_doesnt_exists(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" is already free.")

def success_ban(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" has been added to the black list.")

def success_free(word, update):
    update[MESSAGE].reply_text("The word \"" + word + "\" has been removed from the black list.")

def format_words(words, key):
    if key:
        return "\n▪".join(words) 
    return ", ".join(words)

def get_words(words, update):
    logging.info(words)
    size = len(words)
    if size == 0:
        update[MESSAGE].reply_text("There is no banned words yet")
    elif size <=30:
        update[MESSAGE].reply_text("Current banned words: \n▪" + format_words(words, True))
    else:
        update[MESSAGE].reply_text("Current banned words:\n" + format_words(words, False))

def user_unauthorized(update):
    update[MESSAGE].reply_text("Only administrators can use this command")

def censored_message(update, chat_id, sender, text, banned_words):
    response = ""
    for word in text:
        if banned_words.get(clean_word(word)):
            response = response + "****"
        else:
            response = response + word
        response = response + " "

    update.send_message(chat_id=chat_id, text="@"+ sender.username+"\n"+str(response))

def empty_bl(update):
    update[MESSAGE].reply_text("The black list is already clean")

def free_all_words(update):
    update[MESSAGE].reply_text("Now the black list is all empty")