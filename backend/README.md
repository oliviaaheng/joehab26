# Unserious - AI-Powered Social Trip Planner

An intelligent travel companion that helps you discover, plan, and share your adventures with personalized recommendations and a vibrant community.

## Overview

Unserious transforms trip planning from a tedious task into an interactive experience. By combining AI-powered recommendations, preference learning, and social sharing, we help travelers create memorable itineraries tailored to their unique interests and constraints.

## Key Features

### Intelligent Itinerary Generation
- **Natural Language Input**: Simply describe your trip - destination, dates, accommodation, budget, and preferences
- **AI-Powered Recommendations**: Leverages Gemini API to suggest personalized activities based on your constraints
- **Interactive Preference Learning**: "This or That" interface helps the system understand your travel style
- **Smart Scheduling**: Automatically generates optimized day schedules based on your preferences

### Trip Documentation
- **Photo Scrapbook**: Attach photos and notes to each activity in your itinerary
- **Location Verification**: Uses image metadata to confirm you visited planned locations
- **Memory Collection**: Automatically compiles your trip into a beautiful visual story

### Social & Community Features
- **Share Itineraries**: Publish your travel plans for others to follow and adapt
- **Profile System**: Showcase your travel adventures and discover like-minded explorers
- **Brown University Community**: Special features for students to share local recommendations
- **Follow Travelers**: Connect with others and get inspired by their journeys

### Personalization
- **Preference Profiling**: System learns whether you're adventurous, relaxed, foodie-focused, etc.
- **Smart Recommendations**: Get activity suggestions based on your travel personality
- **Dietary & Accessibility**: Accounts for dietary restrictions and accessibility needs
- **Budget Awareness**: Filters options based on your spending preferences

## System Architecture

### Data Models

**Constraints**
```
- destination: string
- date_of_travel: Date
- address: string (accommodation)
- freeform_text: string (preferences)
```

**Event**
```
- name: string
- description: string
- address: string
- website: string
- image: string (URL)
- cost: string
- category: string
```

**Itinerary**
```
- events: list[(Event, start_time, end_time, pictures)]
```

### API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/generate_activities` | Input: Constraints → Output: list[Event] |
| `/generate_itinerary` | Input: Constraints, scored Events → Output: Itinerary |
| `/upload_itinerary` | Input: username, Itinerary → Output: Itinerary_ID |
| `/get_itineraries` | Input: username → Output: list[Itinerary_ID] |
| `/fetch_itinerary` | Input: itinerary_ID → Output: Itinerary |
| `/update_itinerary` | Input: username, itinerary_ID, Itinerary → Output: OK |

## Tech Stack

- **Backend**: Python server with Gemini API integration
- **Database**: Stores itineraries, events, and user profiles
- **AI/ML**: Google Gemini API for intelligent activity recommendations
- **Frontend**: Interactive web interface with preference selection UI

## Getting Started

### Prerequisites
- Python 3.x
- Gemini API key
- Database setup (MySQL/PostgreSQL)

### Installation

1. Clone the repository
```bash
git clone [your-repo-url]
cd unserious
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables
```bash
# Create .env file
GEMINI_API_KEY=your_api_key_here
TESTING=0  # 0 for Gemini+DB, 1 for testing mode
```

4. Initialize the database
```bash
python setup_db.py
```

5. Run the server
```bash
python server.py
```

## User Flow

1. **Input Travel Details**: Enter destination, dates, accommodation, and preferences
2. **Preference Quiz**: Answer "This or That" questions to help AI understand your travel style
3. **Review Activities**: Swipe through suggested events, indicating likes/dislikes
4. **Generate Itinerary**: AI creates optimized schedule based on your selections
5. **Customize**: Use natural language to modify the itinerary
6. **Experience & Document**: Take photos at locations and build your travel scrapbook
7. **Share**: Publish your itinerary for the community to discover

## Demo Scenarios

The project includes three pre-loaded demo itineraries:

1. **Porto, Portugal** - March, Hotel stay
   - Profile: Relaxed traveler, tourist sites focused

2. **Providence, Rhode Island** - February, Brown University
   - Profile: College student, nature lover, music enthusiast
   - Features photo-taking demo

3. **Atlantic City, New Jersey** - July, Hotel stay
   - Profile: Vegetarian, family-friendly, beach activities

## Contributing

We welcome contributions! This project was built during a hackathon and represents our vision for making travel planning more social, intelligent, and fun.

## License

[Add your license here]

## Team

[Add team member names and roles]

## Acknowledgments

- Google Gemini API for powering our AI recommendations
- Brown University community for inspiration
- All the travelers who make exploration exciting

---

*Built at [Hackathon Name]*