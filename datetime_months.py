# James Lovie 2018 - Current & Previous Dates, Monthly Range Calculator.

import calendar
import datetime

def datetimeFunction(first_day=None, last_day=None, first_day_preceeding=None, last_day_preceeding=None):

	# Find the first and last days of the current month.
	today = datetime.date.today()
	print('Now: ' + str(today))
	monthshift = 1

	strg = '{:%Y-%m-%d}'.format(today)

	year = strg[0:4]
	month = strg[5:7]

	first = today.replace(day=1)
	lastmonth = first - datetime.timedelta(days=1)
	lastYear = lastmonth.strftime("%Y")
	lastmonth = lastmonth.strftime("%m")

	print(str('The Year is: ' + year))
	print(str('The Month is: ' + month))
	print(str('The Preceeding Year is: ' + str(lastYear)))
	print(str('The Preceeding Month is: ' + str(lastmonth)))

	_, num_days = calendar.monthrange(2019, int(month))
	first_day = datetime.date(int(year), int(month), 1)
	last_day = datetime.date(int(year), int(month), num_days)

	_, num_days_preceeding = calendar.monthrange(int(lastYear), int(lastmonth))
	first_day_preceeding = datetime.date(int(lastYear), int(lastmonth), 1)
	last_day_preceeding = datetime.date(int(lastYear), int(lastmonth), num_days_preceeding)

	sqldate = '{:%Y-%m-%d}'
	sqldatetime = '{:%Y-%m-%d-%H-%M-%S}'
	apidate = '{:%Y-%m-%d}'
	apidatetime = '{:%Y-%m-%d-%H-%M-%S}'

	# print('The start of the current month is: ' + str(first_day))
	# print('The end of the current month is: ' + str(last_day))
	# print('The start of the previous month is: ' + str(first_day_preceeding))
	# print('The end of the previous month is: ' + str(last_day_preceeding))

	return str(first_day), str(last_day), str(first_day_preceeding), str(last_day_preceeding)

def main():
    datetimeFunction()

if __name__ == '__main__':
    main()
