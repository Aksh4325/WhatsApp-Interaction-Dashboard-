# WhatsApp Chat Analyzer - Setup Guide

## Complete Installation Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

### Step-by-Step Setup

#### 1. Clone or Download the Project
```bash
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

#### 2. Create Virtual Environment
Creating a virtual environment is recommended to avoid conflicts with system packages.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

#### 4. Download TextBlob Corpora
TextBlob requires additional data for sentiment analysis:
```bash
python -m textblob.download_corpora
```

#### 5. Verify Installation
Run a quick test:
```bash
python main.py
```

You should see the main menu. Select option 1 to test with the sample data.

---

## Exporting Your WhatsApp Chat

### On Android:
1. Open WhatsApp
2. Open the chat you want to analyze
3. Tap the three dots (⋮) in the top right
4. Select **More** → **Export chat**
5. Choose **Without Media**
6. Save the .txt file

### On iPhone:
1. Open WhatsApp
2. Open the chat
3. Tap the contact/group name at the top
4. Scroll down and tap **Export Chat**
5. Choose **Without Media**
6. Save to Files app

### Using Your Exported Chat:
- Place the exported .txt file in the `data/` folder
- When running the program, enter the file path when prompted
- Example: `data/my_chat.txt`

---

## Running the Application

### Basic Usage
```bash
python main.py
```

### Menu Options Explained

**1. Overall Analysis**
- Shows total messages, users, date range
- Displays most active user
- Peak chatting hours
- User contribution percentages
- Message type distribution

**2. User-specific Analysis**
- Select any user from the chat
- View their statistics
- Top words they use
- Activity patterns

**3. Generate All Visualizations**
- Creates 11 different charts
- Saves in `output/` directory
- High-resolution PNG files
- Takes about 10-15 seconds

**4. SQL Insights**
- Monthly message growth
- Inactive periods
- Hourly activity breakdown
- Raw SQL query results

**5. Advanced Text Analysis**
- Common word pairs (bigrams)
- Emoji usage statistics
- Sentiment analysis results

---

## Understanding the Output

### Visualizations Generated

1. **monthly_trend.png**: Line chart showing message volume over months
2. **daily_heatmap.png**: Heatmap of day vs hour activity
3. **user_hour_heatmap.png**: User activity by hour
4. **word_frequency.png**: Top 20 most common words
5. **wordcloud.png**: Visual word frequency cloud
6. **emoji_frequency.png**: Most used emojis
7. **sentiment_distribution.png**: Positive/Neutral/Negative breakdown
8. **conversation_density.png**: Messages per day over time
9. **rolling_average.png**: 7-day moving average
10. **user_contribution.png**: Pie chart of user participation
11. **weekday_distribution.png**: Activity by day of week

### Database Structure

The SQLite database (`database/chat_data.db`) contains:

**Table: messages**
- id (Primary Key)
- datetime
- date
- time
- hour
- day_name
- month
- year
- user
- message
- message_type
- message_length
- word_count

---

## Troubleshooting

### Common Issues

**1. "No module named 'textblob'"**
```bash
pip install textblob
python -m textblob.download_corpora
```

**2. "No messages found"**
- Check if your file format matches Indian WhatsApp format
- Ensure date format is DD/MM/YYYY
- Time should be in 12-hour format with am/pm

**3. "Database connection error"**
- Make sure `database/` directory exists
- Check write permissions
- Delete existing .db file and try again

**4. Charts not generating**
- Ensure `matplotlib` and `seaborn` are installed
- Check if `output/` directory can be created
- Verify you have enough disk space

### Format Verification

Your WhatsApp export should look like:
```
15/01/2025, 9:23 am - Rahul Sharma: Hey everyone!
15/01/2025, 9:25 am - Priya Singh: Good morning!
```

**NOT like:**
```
[15/01/2025, 9:23:45 AM] Rahul Sharma: Hey everyone!
```

---

## Performance Notes

- **Small chats** (< 1,000 messages): Instant analysis
- **Medium chats** (1,000 - 10,000): 5-10 seconds
- **Large chats** (> 10,000): 20-30 seconds
- **Visualization generation**: 10-15 seconds regardless of size

---

## Customization

### Changing Stopwords
Edit `src/analysis.py` → `_load_stopwords()` method

### Modifying Visualizations
Edit `src/visualization.py` → individual plot methods

### Adding New SQL Queries
Edit `src/database.py` → add new query methods

### Adjusting Color Schemes
In `visualization.py`, modify the `plt.style.use()` or `sns.set_palette()` calls

---

## GitHub Upload Checklist

Before uploading to GitHub:

- [ ] Remove any personal chat files from `data/`
- [ ] Keep only `sample_chat.txt` in `data/`
- [ ] Delete `database/` directory (will be auto-created)
- [ ] Delete `output/` directory (will be auto-created)
- [ ] Ensure `.gitignore` is present
- [ ] Update README with your information
- [ ] Check all file paths are relative (not absolute)

---

## Suggested Git Commit Messages

When building this project incrementally:

```bash
git add .
git commit -m "Initial commit: Project structure setup"

git commit -m "Add WhatsApp parser module"

git commit -m "Implement SQLite database integration"

git commit -m "Add advanced analytics features"

git commit -m "Implement visualization module"

git commit -m "Create main application interface"

git commit -m "Add sample chat data and documentation"

git commit -m "Update README with detailed instructions"

git commit -m "Final polish and code cleanup"
```

---

## Directory Permissions

Ensure these directories are writable:
- `database/` - for SQLite database
- `output/` - for generated charts

They will be auto-created if missing.

---

## Academic Presentation Tips

When presenting this project:

1. **Start with the problem**: Explain why chat analysis is useful
2. **Show the data flow**: Parse → Database → Analysis → Visualization
3. **Demonstrate SQL queries**: Show how data is queried efficiently
4. **Highlight analytics**: Focus on insights, not just code
5. **Show visualizations**: Let the charts tell the story
6. **Discuss challenges**: Parsing formats, data cleaning, etc.

---

## Future Enhancements (Ideas)

- Add network graph of user interactions
- Implement response time analysis
- Create weekly/monthly reports
- Add export to PDF functionality
- Multi-language support
- Web interface using Flask (minimal HTML)

---

## Credits

**Libraries Used:**
- Pandas: Data manipulation
- Matplotlib/Seaborn: Visualization
- TextBlob: Sentiment analysis
- WordCloud: Word cloud generation
- SQLite: Data storage

---

## Support

For issues or questions:
- Email: akshay.tiwari@example.com
- Create an issue on GitHub

---

**Good luck with your project presentation!**

© 2026 Akshay Tiwari. All Rights Reserved.
