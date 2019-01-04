import sqlite3
from datetime import datetime


def diff_month(d1, d2):
    """

    :rtype: object
    """
    months_apart = (d1.year - d2.year) * 12 + d1.month - d2.month
    day = 1
    month = d2.month
    year = d2.year
    if months_apart > 1:
        print "****************************************************************************************"
        for x in range(1, months_apart):

            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
            d3 = datetime(year, month , 1)
            if engine_count != 1:
              print "----------NO DATA-----------------", "{:>16s}".format(d3.strftime('%B %Y')), "----------- NO DATA ------------------"

    return months_apart


def get_iso_date(engine_date):
    year_codes = { '1': '1968', '2': '1969', '3': '1970', '4' : '1971', '5': '1972', '6': '1973', '7': '1974' }
    year_key = engine_date[0]
    year = year_codes[year_key]
    month_numeric = engine_date[1:3]
    day_numeric = engine_date[6:8]
    month_index = ((int(year_key) - 1)*12 + int(month_numeric)) - 1  # array starts at zero , january 1968
    monthly_totals_list[month_index] += 1
    return year + "-" + month_numeric + "-" + day_numeric


def main():
    conn = sqlite3.connect('engine_register.db')
    cursor = conn.cursor()
    sql = "select * from engines"
    results = cursor.execute(sql)
    engine_nos = results.fetchall()
    global monthly_totals_list
    monthly_totals_list = ()
    monthly_totals_list = [0] * 120  # 10 years or 120 months up to 1978
    engine_nos_iso = {}
    for engine in engine_nos:              # create parallel dictionary in iso date format so can sort by value later
        amc_code = engine[1]
        engine_nos_iso[engine] = get_iso_date(amc_code)
    start_date_string = "1967-01-01"   # Here's when American Motors started putting dates on their engines
    date_object = datetime.strptime(start_date_string, '%Y-%m-%d')
    last_month = date_object.strftime('%B %Y')
    last_month_object = date_object
    global engine_count
    engine_count = 0
    for key, value in sorted(engine_nos_iso.iteritems(), key=lambda (k,v): (v,k)):
       engine_count += 1
       date_object = datetime.strptime(value, '%Y-%m-%d')
       this_month = date_object.strftime('%B %Y')
       full_date = date_object.strftime('%A, %B %d, %Y')
       engine_serial = key[0]
       amc_code = key[1]
       body_no = key[2]
       casting_no = key[3]
       contact = key[4]
       if (this_month != last_month): # and (last_month != first_month):
         months_apart = diff_month(date_object, last_month_object)
         print "****************************************************************************************"
         print "******************************  " , "{:>16s}".format(this_month) , "  ************************************"
       print "%6s %7s %7s %8s %28s %3s" % (engine_serial, body_no, casting_no, amc_code , full_date , contact)
       last_month = this_month
       last_month_object = date_object


if __name__ == '__main__':
    main()