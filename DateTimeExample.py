from java.time import LocalDate, LocalTime, LocalDateTime
from java.time.temporal import ChronoField
from java.util import Calendar

class DateTimeExample:
    def test_LocalDate(self):
        ld1, ld2 = None, None
        ld1 = LocalDate.now()
        ld2 = LocalDate.of(2010, 10, 10)
        self.print_LocalDate(ld1)
        self.print_LocalDate(ld2)


    def print_LocalDate(self, ld = LocalDate.now()):
        year = ld.get(ChronoField.YEAR)
        month = ld.get(ChronoField.MONTH_OF_YEAR)
        day = ld.get(ChronoField.DAY_OF_MONTH)
        print("<<LocalDate>>")
        print("year = {0}".format(year))
        print("month = {0}".format(month))
        print("day = {0}".format(day))
        print("")

    def test_LocalTime(self):
        lt1 , lt2 = None , None
        lt1 = LocalTime.now()
        lt2 = LocalTime.of(10, 10, 10)
        self.print_LocalTime(lt1)
        self.print_LocalTime(lt2)

    def print_LocalTime(self, lt = LocalTime.now()):
        hour = lt.get(ChronoField.HOUR_OF_DAY)
        minute = lt.get(ChronoField.MINUTE_OF_HOUR)
        second = lt.get(ChronoField.SECOND_OF_MINUTE)
        ms = lt.get(ChronoField.MILLI_OF_SECOND)
        print("<<LocalTime>>")
        print("hour = {0}".format(hour))
        print("minute = {0}".format(minute))
        print("second = {0}".format(second))
        print("ms = {0}".format(ms))
        print("")


    def test_LocalDateTime(self):
        ldt1 , ldt2 = None , None
        ldt1 = LocalDateTime.now()
        ldt2 = LocalDateTime.of(2010, 10, 10, 10, 10, 10, 10)
        self.print_LocalDateTime(ldt1)
        self.print_LocalDateTime(ldt2)


    def print_LocalDateTime(self, ldt = LocalDateTime.now()):
        year = ldt.get(ChronoField.YEAR)
        month = ldt.get(ChronoField.MONTH_OF_YEAR)
        day = ldt.get(ChronoField.DAY_OF_MONTH)
        hour = ldt.get(ChronoField.HOUR_OF_DAY)
        minute = ldt.get(ChronoField.MINUTE_OF_HOUR)
        second = ldt.get(ChronoField.SECOND_OF_MINUTE)
        ms = ldt.get(ChronoField.MILLI_OF_SECOND)
        print("<<LocalDateTime>>")
        print("year = {0}".format(year))
        print("month = {0}".format(month))
        print("day = {0}".format(day))
        print("hour = {0}".format(hour))
        print("minute = {0}".format(minute))
        print("second = {0}".format(second))
        print("ms = {0}".format(ms))
        print("")


    def test_Calendar(self):
        cl1  = Calendar.getInstance()
        print("current date = {0}".format(cl1.getTime()))
        cl1.add(Calendar.DATE, 1)
        print("cl1 + 1 date = {0}".format(cl1.getTime()))
        cl1.add(Calendar.DATE, -15)
        print("cl1 - 15 date = {0}".format(cl1.getTime()))
        cl1.add(Calendar.MONTH, 2)
        print("cl1 + 2 month = {0}".format(cl1.getTime()))
        cl1.add(Calendar.YEAR, 10)
        print("cl1 + 10 year = {0}".format(cl1.getTime()))
        print("")
        self.print_Calendar(cl1)

    def print_Calendar(self, cl = Calendar.getInstance()):
        year = cl.get(Calendar.YEAR)
        month = cl.get(Calendar.MONTH)
        day = cl.get(Calendar.DATE)
        hour = cl.get(Calendar.HOUR)
        minute = cl.get(Calendar.MINUTE)
        second = cl.get(Calendar.SECOND)
        ms = cl.get(Calendar.MILLISECOND)
        print("<<Calendar>>")
        print("year = {0}".format(year))
        print("month = {0}".format(month))
        print("day = {0}".format(day))
        print("hour = {0}".format(hour))
        print("minute = {0}".format(minute))
        print("second = {0}".format(second))
        print("millisecond = {0}".format(ms))
        print("")