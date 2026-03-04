# Link Scraper

A Django web application that scrapes and collects all links from a given website URL. Simply enter a website address, and the application will extract all links and display them in a searchable table.

## Features

- **Web Scraping**: Extract all links from any website URL
- **Data Storage**: Store scraped links in a SQLite database
- **Link Management**: View, search, and manage collected links
- **Bulk Delete**: Clear all collected links with a single action
- **Responsive UI**: Clean, modern interface built with Tailwind CSS
- **Error Handling**: Graceful handling of invalid URLs and scraping errors

## Tech Stack

- **Framework**: Django 6.0.2
- **Database**: SQLite
- **Web Scraping**: BeautifulSoup 4, Requests
- **Frontend**: Tailwind CSS
- **Python**: 3.8+

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/darshan3187/Link_Scraper.git
   cd Link_Scraper
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django requests beautifulsoup4
   ```

4. **Navigate to the project directory**
   ```bash
   cd mysite
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage

### Basic Usage

1. **Scrape Links**
   - Enter a website URL (e.g., `https://example.com`)
   - Click the "Scrape" button
   - The application will extract all links from the page and display them in a table

2. **View Results**
   - All scraped links are displayed in a table with:
     - Link ID
     - Link Name/Text
     - Link URL
   - Links are displayed in reverse chronological order (newest first)

3. **Delete Links**
   - Click the "Delete All" button to remove all links from the database
   - This action cannot be undone

### Example

```
Input: https://github.com
Output: Table showing all links found on the GitHub homepage
```

## Project Structure

```
Link_Scraper/
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── mysite/                 # Django project directory
│   ├── manage.py           # Django management script
│   ├── db.sqlite3          # SQLite database
│   ├── myapp/              # Main application
│   │   ├── models.py       # Link model definition
│   │   ├── views.py        # View logic for scraping and display
│   │   ├── admin.py        # Django admin configuration
│   │   ├── urls.py         # URL routing
│   │   ├── templates/      # HTML templates
│   │   │   └── myapp/
│   │   │       └── result.html
│   │   └── migrations/     # Database migrations
│   └── mysite/             # Django settings directory
│       ├── settings.py     # Project settings
│       ├── urls.py         # URL configuration
│       └── wsgi.py         # WSGI application
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Display all scraped links |
| `/` | POST | Submit URL to scrape links |
| `/delete/` | GET | Delete all links |
| `/admin/` | GET | Django admin interface |

## Data Model

### Link Model

The application stores links with the following fields:

- **id**: Auto-generated primary key
- **name**: Text content of the link (max 255 characters)
- **address**: URL of the link (max 500 characters)

## Limitations and Notes

- The scraper only extracts links that are properly formatted in the HTML (`<a>` tags with `href` attributes)
- Relative URLs are stored as-is; they may need to be resolved to absolute URLs for access
- The application stores all links from a page, including navigation links, footer links, etc.
- Large websites with thousands of links may take time to process

## Troubleshooting

### Issue: Connection Error when scraping

**Solution**: Verify the URL is valid and accessible. Some websites may block scraping requests.

### Issue: Links not appearing

**Solution**: Check that:
- The URL is valid and accessible
- The website contains links
- No network errors occurred during scraping

### Issue: Database locked error

**Solution**: Close any other instances of the application using the database and try again.

## Development and Contributing

### Setting up for development

1. Follow the installation steps above
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and test thoroughly
4. Commit your changes:
   ```bash
   git commit -m "Add descriptive commit message"
   ```
5. Push to your fork and submit a pull request

### Basic development commands

```bash
# Create a Django app
python manage.py startapp appname

# Create migrations for model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run tests
python manage.py test

# Access Django shell
python manage.py shell

# Create a superuser for admin
python manage.py createsuperuser
```

## Admin Interface

Access the Django admin panel at `/admin/` to:
- View, edit, and delete links manually
- Create user accounts
- Manage application settings

## License

This project is provided as-is for educational and personal use.

## Author

**Darshan** - [@darshan3187](https://github.com/darshan3187)

## Support

For issues, questions, or suggestions:
- Open an issue on the [GitHub repository](https://github.com/darshan3187/Link_Scraper/issues)
- Check existing issues for solutions

## Future Enhancements

Potential features for future versions:
- Export scraped links to CSV/Excel
- Filter and search collected links
- Schedule automatic scraping
- Support for JavaScript-rendered content
- Link validation and status checking
- Database backup and restore functionality
