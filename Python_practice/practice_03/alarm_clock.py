"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating 
if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring.
Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) == '7:00'
alarm_clock(5, False) == '7:00'
alarm_clock(0, False) == '10:00'

"""

def weekdays(choice):
	return {0 : 'Sun', 1 : 'Mon', 2 : 'Tue', 3 : 'Wed', 4 : 'Thurs', 5 : 'Fri', 6 : 'Sat'}


def alarm_clock(weekday, is_on_vacation):
	if is_on_vacation:
		if weekday in (0, 6):
			return 'off'
		else:
			return '10:00'
	else:
		if weekday in (0, 6):
			return '10:00'
		else:
			return '7:00'



def test_alarm_clock():
	assert alarm_clock(1, False) == '7:00'
	assert alarm_clock(5, False) == '7:00'
	assert alarm_clock(0, False) == '10:00'


# test_alarm_clock()