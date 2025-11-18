# Medical Appointment Scheduling Agent 🏥

A FastAPI-based intelligent appointment scheduling system that integrates with Calendly API and provides conversational booking capabilities with FAQ support using RAG (Retrieval Augmented Generation).

## 🚀 Features

- **Smart Appointment Scheduling**: Book medical appointments with automatic slot suggestions
- **Calendly Integration**: Seamless integration with Calendly API for real-time availability
- **Conversational AI**: Chat-based interface for natural language appointment booking
- **FAQ Support**: AI-powered FAQ system using RAG for clinic information queries
- **Multiple Appointment Types**: Support for consultations, follow-ups, physical exams, and specialist visits
- **Real-time Availability**: Check doctor availability and suggest optimal time slots
- **RESTful API**: Well-documented API endpoints for integration

## 🏗️ Architecture

```
appointment-scheduling-agent/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── agent/
│   │   ├── scheduling_agent.py # Core scheduling logic
│   │   └── prompts.py         # AI prompts and templates
│   ├── api/
│   │   ├── chat.py            # Chat endpoints for booking
│   │   └── calendly_integration.py # Calendly API integration
│   ├── models/
│   │   └── schemas.py         # Pydantic data models
│   ├── rag/
│   │   ├── faq_rag.py        # FAQ retrieval system
│   │   ├── vector_store.py   # Vector storage and retrieval
│   │   └── embeddings.py     # Text embedding utilities
│   └── tools/
│       ├── availability_tool.py # Availability checking
│       └── booking_tool.py      # Appointment booking
├── data/
│   ├── clinic_info.json       # Clinic FAQ and information
│   └── doctor_schedule.json   # Doctor schedule data
└── tests/
    └── test_agent.py          # Unit tests
```

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dip4836/Medical-Appointment-Scheduling-Agent-.git
   cd appointment-scheduling-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables** (Optional)
   Create a `.env` file:
   ```env
   BACKEND_PORT=8000
   CALENDLY_API_KEY=your_calendly_api_key
   ```

## 🚀 Usage

### Starting the Server

```bash
python -m backend.main
```

The API will be available at `http://localhost:8000`

### API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI).

## 📚 API Endpoints

### Chat Endpoints

#### Get Appointment Suggestions
```http
GET /api/chat/suggest?date=2025-11-19&appointment_type=consultation
```

**Response:**
```json
{
  "date": "2025-11-19",
  "suggested_slots": [
    {
      "start_time": "09:00",
      "end_time": "09:30",
      "available": true,
      "doctor": "Dr. Smith"
    }
  ]
}
```

#### Book Appointment
```http
POST /api/chat/book
Content-Type: application/json

{
  "appointment_type": "consultation",
  "date": "2025-11-19",
  "start_time": "09:00",
  "patient": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "1234567890"
  },
  "reason": "Regular checkup"
}
```

#### FAQ Query
```http
POST /api/chat/faq
Content-Type: application/json

{
  "q": "What insurance do you accept?"
}
```

### Calendly Integration

#### Check Availability
```http
GET /api/calendly/availability?date=2025-11-19&appointment_type=consultation
```

## 🎯 Appointment Types

The system supports multiple appointment types with different durations:

- **Consultation**: 30 minutes - General medical consultation
- **Follow-up**: 15 minutes - Follow-up visit
- **Physical**: 45 minutes - Physical examination
- **Specialist**: 60 minutes - Specialist consultation

## 🤖 AI Features

### RAG-Powered FAQ System

The system includes an intelligent FAQ system that can answer questions about:

- Clinic location and hours
- Insurance and billing information
- Visit preparation requirements
- Clinic policies and procedures

### Smart Slot Suggestions

The AI agent automatically:
- Analyzes available time slots
- Considers appointment type and duration
- Suggests optimal booking times
- Handles scheduling conflicts

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

Run specific tests:
```bash
pytest tests/test_agent.py -v
```

## 📊 Data Models

### Patient Information
```python
{
  "name": "string",
  "email": "string",
  "phone": "string"
}
```

### Booking Request
```python
{
  "appointment_type": "consultation|followup|physical|specialist",
  "date": "YYYY-MM-DD",
  "start_time": "HH:MM",
  "patient": {Patient},
  "reason": "string"
}
```

## 🔧 Configuration

### Clinic Information

Edit `data/clinic_info.json` to customize:
- Clinic details and location
- Insurance and billing information
- Visit preparation guidelines
- Clinic policies

### Doctor Schedules

Modify `data/doctor_schedule.json` to configure:
- Doctor availability
- Working hours
- Appointment slots

## 🌐 CORS Configuration

The application is configured with permissive CORS settings for development. For production, update the CORS middleware in `backend/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## 🔌 Integration

### Calendly Setup

1. Get your Calendly API key from the Calendly developer portal
2. Set the `CALENDLY_API_KEY` environment variable
3. Update the Calendly endpoints in `backend/api/calendly_integration.py`

## 📈 Monitoring & Logging

The application uses FastAPI's built-in logging. For production deployments, consider adding:

- Structured logging with JSON format
- Application performance monitoring (APM)
- Health check endpoints
- Metrics collection

## 🚀 Deployment

### Docker (Recommended)

Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "-m", "backend.main"]
```

### Cloud Deployment

The application can be deployed to:
- **Heroku**: Use the provided `Procfile`
- **AWS Lambda**: With FastAPI adapter
- **Google Cloud Run**: Container-based deployment
- **Azure App Service**: Python web app

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:

- **Issues**: [GitHub Issues](https://github.com/Dip4836/Medical-Appointment-Scheduling-Agent-/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Dip4836/Medical-Appointment-Scheduling-Agent-/discussions)
- **Email**: [Your contact email]

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] SMS notifications
- [ ] Calendar synchronization
- [ ] Advanced scheduling algorithms
- [ ] Patient portal integration
- [ ] Telemedicine support
- [ ] Analytics dashboard
- [ ] Mobile application

---

**Made with ❤️ for better healthcare accessibility**