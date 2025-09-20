# Jovian Careers Website

## Overview
A professional careers website built with Flask for Jovian company. The website showcases job opportunities, company information, and provides a platform for potential candidates to learn about the organization.

## Current State
- **Status**: Fully functional and deployed
- **Framework**: Flask (Python)
- **Server**: Running on port 5000
- **Last Updated**: September 20, 2025

## Recent Changes
- September 20, 2025: Initial project setup and complete implementation
  - Created Flask application with proper routing
  - Implemented responsive HTML templates using Jinja2
  - Added professional CSS styling with mobile responsiveness
  - Configured for Replit environment with host 0.0.0.0:5000
  - Set up autoscale deployment configuration

## Project Architecture

### Directory Structure
```
├── app.py                 # Main Flask application
├── templates/             # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── jobs.html         # Jobs listing page
│   ├── about.html        # About company page
│   └── contact.html      # Contact information page
├── static/
│   └── css/
│       └── style.css     # Main stylesheet
├── pyproject.toml        # Python project configuration
├── uv.lock              # Dependency lock file
└── replit.md            # This documentation file
```

### Key Features
- **Home Page**: Hero section with company overview and feature highlights
- **Jobs Page**: Dynamic job listings with sample positions
- **About Page**: Company mission, values, and culture information
- **Contact Page**: Contact form and company contact details
- **Responsive Design**: Mobile-friendly layout that works on all devices

### Technical Details
- **Flask Routes**: 
  - `/` - Home page
  - `/jobs` - Job listings with sample data
  - `/about` - Company information
  - `/contact` - Contact page with form
- **Hosting**: Configured for 0.0.0.0:5000 to work with Replit proxy
- **Deployment**: Autoscale configuration for production deployment
- **Styling**: Modern CSS with responsive grid layouts and smooth transitions

### Sample Data
The jobs page includes sample job listings for demonstration:
- Senior Python Developer (Engineering, Remote)
- Data Scientist (Analytics, San Francisco)
- UX Designer (Design, New York)
- Marketing Coordinator (Marketing, Remote)

## Development Setup
The project is fully configured for the Replit environment:
1. Python 3.11 with Flask installed
2. Workflow configured to run `python app.py`
3. Server automatically starts on port 5000
4. All dependencies managed through uv

## User Preferences
- Clean, professional design aesthetic
- Mobile-first responsive approach
- Modern Flask development practices
- Clear navigation and user experience

## Future Enhancements
Potential improvements could include:
- Database integration for dynamic job management
- User authentication and application system
- Admin panel for job posting management
- Email contact form functionality
- SEO optimization and meta tags