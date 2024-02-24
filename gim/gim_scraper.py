import mechanicalsoup as msoup

class GIMScraper:
    """Class used to encapsulate web scraper for the UNS GIM web page (http://gim.ftn.uns.ac.rs)
    """

    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password
        self.__browser = msoup.StatefulBrowser()
        self.__url = 'http://gim.ftn.uns.ac.rs'
        self.__current_page = self.__browser.get(self.__url)

    def exam_appointments_status(self, professor_id: int = 1) -> list:
        """Gets the number of exam appointments per available date

        Parameters:
            professor_id (int): Declares which professor's appointments are you searching from. Default: 1.

        Returns: 
            list: list of tuples (date, number_of_appointments)
        """

        if not self.__check_login_status():
            self.__login()

        self.__navigate(f'{self.__url}/IzmenaZakazanogTermina?nastavnik={professor_id}')
        
        appointment_soup = self.__current_page.soup
        date_select = appointment_soup.find('select', {'name': 'datum'})
        date_options = date_select.select('option')

        dates_with_timeslots = []
        for date_opt in date_options:
            date = date_opt.text.strip()
            timeslot_num = self.number_of_appointments(date, professor_id)
            if timeslot_num > 0:
                dates_with_timeslots.append((date, timeslot_num))

        return dates_with_timeslots

    def number_of_appointments(self, date: str, professor_id: int) -> int:
        """Gets the number of exam appointments for a choosen date

        Parameters:
            date (str): appointment date
            professor_id (int): choosen professor

        Returns: 
            int: number of appointments for selected date
        """

        self.__navigate(f'{self.__url}//IzmenaZakazanogTermina?nastavnik={professor_id}&datum={date}')
        timeslots_soup = self.__current_page.soup

        timeslot_select = timeslots_soup.find('select', {'name': 'vreme'})
        if not timeslot_select:
            return 0
        
        timeslots = timeslot_select.select('option')
        return len(timeslots)

    def __login(self) -> None:
        self.__navigate(f'{self.__url}/Prijava?povratniUrl=?')
        login_soup = self.__current_page.soup
        form = login_soup.find('form', {'name': 'prijava'})
        form.find('input', {'name': 'korisnickoIme'})['value'] = self.__username
        form.find('input', {'name': 'lozinka'})['value'] = self.__password
        
        self.__current_page = self.__browser.submit(form, self.__current_page.url)

    def __navigate(self, url: str) -> None:
        self.__current_page = self.__browser.get(url)

    def __check_login_status(self) -> bool:
        page = self.__browser.get(f'{self.__url}/Nalog')
        return page.url == f'{self.__url}/Nalog'