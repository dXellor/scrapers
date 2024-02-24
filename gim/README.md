<a id="gim_scraper"></a>

# gim\_scraper

<a id="gim_scraper.GIMScraper"></a>

## GIMScraper Objects

```python
class GIMScraper()
```

Class used encapsulate web scraper for the UNS GIM web page (http://gim.ftn.uns.ac.rs)

<a id="gim_scraper.GIMScraper.exam_appointments_status"></a>

#### exam\_appointments\_status

```python
def exam_appointments_status(professor_id: int = 1) -> list
```

Gets the number of exam appointments per available date

**Arguments**:

- `professor_id` _int_ - Declares which professor's appointments are you searching from. Default: 1.
  

**Returns**:

- `list` - list of tuples (date, number_of_appointments)

<a id="gim_scraper.GIMScraper.number_of_appointments"></a>

#### number\_of\_appointments

```python
def number_of_appointments(date: str, professor_id: int) -> int
```

Gets the number of exam appointments for a choosen date

**Arguments**:

- `date` _str_ - appointment date
- `professor_id` _int_ - choosen professor
  

**Returns**:

- `int` - number of appointments for selected date

