"""
WhatsApp Chat Analyzer - Main Application
College Data Analytics Project
"""

import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from parser import WhatsAppParser
from database import ChatDatabase
from analysis import ChatAnalyzer
from visualization import ChatVisualizer
from utils import *


def load_and_process_data(file_path):
    """Load and process WhatsApp chat data"""
    print_header("LOADING AND PROCESSING DATA")
    
    # Parse chat file
    print("→ Parsing WhatsApp chat file...")
    parser = WhatsAppParser(file_path)
    df = parser.get_clean_data()
    
    if df is None or len(df) == 0:
        print_error("Failed to parse chat file. Please check the format.")
        return None, None
    
    print_success(f"Parsed {len(df)} messages successfully")
    
    # Store in database
    print("\n→ Storing data in SQLite database...")
    db = ChatDatabase()
    db.connect()
    db.insert_data(df)
    
    print_success("Data processing complete!")
    
    return df, db


def show_overall_analysis(df, db):
    """Display overall chat analysis"""
    print_header("OVERALL CHAT ANALYSIS")
    
    # Basic statistics
    print_subheader("Basic Statistics")
    stats = {
        'Total Messages': len(df),
        'Total Users': df['user'].nunique(),
        'Date Range': f"{df['date'].min()} to {df['date'].max()}",
        'Text Messages': len(df[df['message_type'] == 'text']),
        'Media Shared': len(df[df['message_type'] == 'media']),
        'Deleted Messages': len(df[df['message_type'] == 'deleted'])
    }
    print_stats_table(stats)
    
    # SQL Insights
    print_subheader("SQL Query Insights")
    
    # Most active user
    most_active = db.get_most_active_user()
    print(f"\nMost Active User: {most_active['user'].values[0]} ({most_active['message_count'].values[0]} messages)")
    
    # Average messages per day
    avg_msgs = db.get_messages_per_day()
    print(f"Average Messages per Day: {avg_msgs:.2f}")
    
    # Peak hour
    peak = db.get_peak_hour()
    hour = peak['hour'].values[0]
    time_period = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12
    if display_hour == 0:
        display_hour = 12
    print(f"Peak Chatting Hour: {display_hour}:00 {time_period} ({peak['message_count'].values[0]} messages)")
    
    # User contribution
    print("\n→ User Contribution Percentage:")
    contribution = db.get_user_contribution()
    for _, row in contribution.iterrows():
        print(f"   {row['user']:<20}: {row['percentage']}%")
    
    # Media vs Text ratio
    print("\n→ Message Type Distribution:")
    media_text = db.get_media_text_ratio()
    for _, row in media_text.iterrows():
        print(f"   {row['message_type'].title():<15}: {row['count']} ({row['percentage']}%)")
    
    # Weekday distribution
    print("\n→ Most Active Days:")
    weekday = db.get_weekday_distribution()
    for idx, row in weekday.head(3).iterrows():
        print(f"   {idx+1}. {row['day_name']:<12}: {row['message_count']} messages")
    
    # Longest message
    longest = db.get_longest_message()
    if len(longest) > 0:
        print(f"\nLongest Message: {longest['message_length'].values[0]} characters by {longest['user'].values[0]}")
    
    input("\nPress Enter to continue...")


def show_user_analysis(df, db):
    """Display user-specific analysis"""
    print_header("USER-SPECIFIC ANALYSIS")
    
    # Show available users
    users = df['user'].unique()
    print("Available Users:")
    for idx, user in enumerate(users, 1):
        print(f"{idx}. {user}")
    
    # Get user selection
    try:
        choice = int(input("\nSelect user number: "))
        if 1 <= choice <= len(users):
            selected_user = users[choice - 1]
        else:
            print_error("Invalid selection")
            return
    except ValueError:
        print_error("Invalid input")
        return
    
    # Analyze user
    analyzer = ChatAnalyzer(df)
    user_stats = analyzer.get_user_statistics(selected_user)
    
    if user_stats is None:
        print_error("No data found for this user")
        return
    
    print_subheader(f"Statistics for {selected_user}")
    print_stats_table(user_stats)
    
    # User-specific word frequency
    user_df = df[df['user'] == selected_user]
    user_analyzer = ChatAnalyzer(user_df)
    
    print("\n→ Top 10 Words Used:")
    word_freq = user_analyzer.get_word_frequency(10)
    for idx, (word, count) in enumerate(word_freq, 1):
        print(f"   {idx}. {word:<15}: {count} times")
    
    input("\nPress Enter to continue...")


def generate_all_visualizations(df, db):
    """Generate all visualization charts"""
    print_header("GENERATING VISUALIZATIONS")
    
    create_directory('output')
    
    analyzer = ChatAnalyzer(df)
    visualizer = ChatVisualizer(df)
    
    print("→ Creating visualizations...\n")
    
    # Generate all charts
    visualizer.plot_monthly_trend(analyzer)
    visualizer.plot_daily_heatmap(analyzer)
    visualizer.plot_user_hour_heatmap(analyzer)
    visualizer.plot_word_frequency(analyzer)
    visualizer.generate_wordcloud(analyzer)
    visualizer.plot_emoji_frequency(analyzer)
    visualizer.plot_sentiment_distribution(analyzer)
    visualizer.plot_conversation_density(analyzer)
    visualizer.plot_rolling_average(analyzer)
    visualizer.plot_user_contribution(db)
    visualizer.plot_weekday_distribution(db)
    
    print_success("\nAll visualizations saved in 'output/' directory")
    input("\nPress Enter to continue...")


def show_sql_insights(db):
    """Display detailed SQL query results"""
    print_header("SQL QUERY INSIGHTS")
    
    print("→ Running analytical queries...\n")
    
    # 1. Monthly growth
    print_subheader("Monthly Message Growth")
    monthly = db.get_monthly_growth()
    print(monthly.to_string(index=False))
    
    # 2. Inactive periods
    print_subheader("\nMost Inactive Days (Least Messages)")
    inactive = db.get_inactive_periods()
    print(inactive.to_string(index=False))
    
    # 3. Hourly activity by user
    print_subheader("\nHourly Activity Summary (Top 10)")
    hourly = db.get_hourly_activity_by_user()
    print(hourly.head(10).to_string(index=False))
    
    input("\n\nPress Enter to continue...")


def show_advanced_analysis(df):
    """Show advanced text analysis"""
    print_header("ADVANCED TEXT ANALYSIS")
    
    analyzer = ChatAnalyzer(df)
    
    # Bigrams
    print_subheader("Top 10 Common Word Pairs (Bigrams)")
    bigrams = analyzer.get_bigrams(10)
    for idx, (bigram, count) in enumerate(bigrams, 1):
        print(f"{idx}. '{bigram}' - {count} times")
    
    # Emoji analysis
    print_subheader("\nTop 10 Emojis Used")
    emojis = analyzer.get_emoji_frequency(10)
    if emojis:
        for idx, (emoji, count) in enumerate(emojis, 1):
            print(f"{idx}. {emoji} - {count} times")
    else:
        print("No emojis found in the chat")
    
    # Sentiment distribution
    print_subheader("\nSentiment Analysis")
    sentiment = analyzer.perform_sentiment_analysis()
    for sent_type, count in sentiment.items():
        print(f"{sent_type}: {count} messages ({count/len(df)*100:.2f}%)")
    
    input("\n\nPress Enter to continue...")


def main():
    """Main application function"""
    clear_screen()
    print_header("WHATSAPP CHAT ANALYZER")
    print("College Data Analytics Project\n")
    
    # Check if sample file exists
    default_file = "data/sample_chat.txt"
    
    if os.path.exists(default_file):
        use_default = input(f"Use sample chat file ({default_file})? (y/n): ").lower()
        if use_default == 'y':
            file_path = default_file
        else:
            file_path = input("Enter WhatsApp chat file path: ")
    else:
        file_path = input("Enter WhatsApp chat file path: ")
    
    if not validate_file_path(file_path):
        print_error("File not found. Exiting...")
        return
    
    # Load and process data
    df, db = load_and_process_data(file_path)
    
    if df is None:
        return
    
    # Main menu loop
    while True:
        clear_screen()
        
        menu_options = [
            "Overall Analysis",
            "User-specific Analysis",
            "Generate All Visualizations",
            "SQL Insights",
            "Advanced Text Analysis"
        ]
        
        display_menu(menu_options)
        choice = get_user_choice(len(menu_options))
        
        if choice == 1:
            show_overall_analysis(df, db)
        elif choice == 2:
            show_user_analysis(df, db)
        elif choice == 3:
            generate_all_visualizations(df, db)
        elif choice == 4:
            show_sql_insights(db)
        elif choice == 5:
            show_advanced_analysis(df)
        elif choice == len(menu_options) + 1:
            print("\nThank you for using WhatsApp Chat Analyzer!")
            db.close()
            print_footer()
            break
    

if __name__ == "__main__":
    main()
