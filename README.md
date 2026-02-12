# WhatsApp Chat Analyzer

A comprehensive data analytics project that analyzes WhatsApp chat exports using Python, SQL, and data visualization libraries. This project was developed as a college-level data analytics portfolio project.

## 📊 Features

### Data Processing
- Parse Indian WhatsApp export format (DD/MM/YYYY, HH:MM am/pm)
- Extract datetime, user, and message information
- Classify messages (text, media, deleted)
- Store processed data in SQLite database

### SQL Analytics (10+ Queries)
- Most active user analysis
- Average messages per day
- Peak chatting hours
- Weekday distribution
- User contribution percentage
- Media vs text message ratio
- Monthly growth trends
- Longest message tracking
- Inactive period detection
- Hourly activity by user

### Advanced Analysis
- Monthly trend analysis
- Daily activity heatmaps
- Hour vs user activity mapping
- Word frequency analysis (with stopword removal)
- Emoji frequency tracking
- Sentiment analysis (Positive/Neutral/Negative)
- Conversation density over time
- 7-day rolling average
- Bigram (word pair) analysis
- User-specific statistics

### Visualizations
- Monthly message trends (line chart)
- Daily activity heatmap
- User-hour activity heatmap
- Word frequency bar chart
- Word cloud generation
- Emoji frequency chart
- Sentiment distribution (pie & bar)
- Conversation density timeline
- Rolling average plot
- User contribution pie chart
- Weekday distribution bar chart

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Database**: SQLite
- **Data Processing**: Pandas
- **Visualization**: Matplotlib, Seaborn
- **Text Analysis**: Regex, TextBlob
- **Word Cloud**: WordCloud

## 📁 Project Structure

```
whatsapp-chat-analyzer/
│
├── data/
│   └── sample_chat.txt          # Sample WhatsApp chat export
│
├── database/
│   └── chat_data.db             # SQLite database (auto-created)
│
├── src/
│   ├── parser.py                # WhatsApp chat parser
│   ├── database.py              # Database operations
│   ├── analysis.py              # Advanced analytics
│   ├── visualization.py         # Chart generation
│   └── utils.py                 # Utility functions
│
├── output/                      # Generated visualizations (auto-created)
│
├── main.py                      # Main application
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── LICENSE                      # MIT License
```

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download TextBlob Data (First-time only)
```bash
python -m textblob.download_corpora
```

## 💻 Usage

### Running the Application
```bash
python main.py
```

### Exporting WhatsApp Chat
1. Open WhatsApp on your phone
2. Go to the chat you want to analyze
3. Tap on three dots (⋮) > More > Export chat
4. Choose "Without Media"
5. Save the .txt file
6. Place it in the `data/` folder

### Menu Options
1. **Overall Analysis**: View comprehensive chat statistics and SQL insights
2. **User-specific Analysis**: Analyze individual user behavior
3. **Generate All Visualizations**: Create all charts and save to `output/`
4. **SQL Insights**: Detailed SQL query results
5. **Advanced Text Analysis**: Bigrams, emojis, and sentiment analysis

## 📈 Sample Output

The application generates various insights including:

- Total messages and users
- Date range of conversation
- Most active participants
- Peak chatting times
- Message type distribution
- Sentiment breakdown
- Word and emoji frequency
- And much more!

All visualizations are saved as high-resolution PNG files in the `output/` directory.

## 🔍 Example Queries

The project includes 10+ SQL queries such as:

```sql
-- Most Active User
SELECT user, COUNT(*) as message_count
FROM messages
GROUP BY user
ORDER BY message_count DESC
LIMIT 1;

-- Peak Hour Analysis
SELECT hour, COUNT(*) as message_count
FROM messages
GROUP BY hour
ORDER BY message_count DESC
LIMIT 1;
```

## 📊 Visualizations

All charts are created using Matplotlib and Seaborn with professional styling:

- Clean and readable layouts
- Proper axis labels and titles
- Color-coded for better understanding
- High DPI (300) for quality output

## 🤝 Contributing

This is a college academic project, but suggestions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Akshay Tiwari**
- Data Analyst
- Email: tiwariaksh25@gmail.com

**Ayush patidar**
- Web Developer
- Email: ayushpatidar@gmail.com

## 🎓 Academic Information

This project was developed as a college data analytics portfolio project to demonstrate:
- Data parsing and cleaning
- SQL database operations
- Advanced statistical analysis
- Data visualization techniques
- Python programming best practices

## 🙏 Acknowledgments

- Thanks to my professors for guidance
- WhatsApp for the chat export feature
- Open-source community for amazing libraries

## ⚠️ Privacy Note

This tool processes WhatsApp chats locally on your machine. No data is uploaded or shared with any third party. Always respect privacy when analyzing group chats.

---

**© 2023 Bherulal Patidar Govt. PG college , Indore. All Rights Reserved.**

*For educational purposes only*
