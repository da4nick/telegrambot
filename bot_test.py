import mainbot
import pytest
import unittest.mock

def test_bot():
    message = unittest.mock.Mock()
    name = 'Пользователь'
    mainbot.username(message)
    name = message.text
    message.send.assert_called_with('Приятно познакомиться, ' + name + '!')