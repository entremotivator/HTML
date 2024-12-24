import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Exclusive Monthly Newsletter",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .section {
            padding: 40px 30px;
            margin: 20px 0;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            background: linear-gradient(90deg, #6A11CB, #2575FC);
            color: white;
            text-align: center;
            padding: 60px;
            font-size: 42px;
            font-weight: bold;
        }
        .intro {
            background-color: #F5F5F5;
            text-align: center;
            font-size: 20px;
            padding: 30px;
            color: #333;
        }
        .section h2 {
            font-size: 28px;
            margin-bottom: 12px;
        }
        .section p, .section li {
            font-size: 18px;
            line-height: 1.6;
        }
        ul {
            margin-left: 20px;
        }
        img {
            max-width: 100%;
            border-radius: 10px;
        }
        a {
            color: #FFCA28;
            text-decoration: none;
        }
        .cta {
            background-color: #0288D1;
            color: white;
            text-align: center;
            padding: 40px;
            font-size: 28px;
        }
        .footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="section header">📢 Exclusive Monthly Newsletter</div>', unsafe_allow_html=True)

# Introduction Section
st.markdown("""
    <div class="section intro">
        <p>Welcome to our latest newsletter, packed with updates, insights, and resources. Whether you're here to learn, engage, or get inspired, we’ve got something for everyone!</p>
    </div>
""", unsafe_allow_html=True)

# Feature Highlight Section
st.markdown("""
    <div class="section feature">
        <h2>🌟 Feature Highlight: Personalized Dashboards</h2>
        <p>Our new personalized dashboards are here to revolutionize your experience! With these features:</p>
        <ul>
            <li>🖥️ Fully customizable widgets for real-time insights.</li>
            <li>📊 Seamless integration with your favorite tools.</li>
            <li>🚀 AI-powered recommendations to boost productivity.</li>
        </ul>
        <p><a href="https://example.com" target="_blank">Learn More</a></p>
    </div>
""", unsafe_allow_html=True)

# Industry Trends Section
st.markdown("""
    <div class="section trends">
        <h2>📈 Latest Industry Trends</h2>
        <p>Stay ahead of the curve with these trending topics:</p>
        <ul>
            <li>🔍 The rise of AI-driven decision-making.</li>
            <li>🌐 The future of remote work technologies.</li>
            <li>📱 Mobile-first strategies taking the lead in 2024.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Community Highlights Section
st.markdown("""
    <div class="section community">
        <h2>💬 Community Highlights</h2>
        <p>Here’s what our amazing community has been up to:</p>
        <ul>
            <li>👏 <b>Project Spotlight:</b> John D. built an AI chatbot that serves 5,000 users daily.</li>
            <li>🌟 <b>Milestone:</b> Over 50,000 members joined our forums this month!</li>
            <li>🎉 <b>Success Story:</b> Jane S. launched her startup using our tools.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Upcoming Events Section
st.markdown("""
    <div class="section events">
        <h2>📅 Upcoming Events</h2>
        <p>Mark your calendars for these exciting events:</p>
        <ul>
            <li>🌍 <b>Global Summit:</b> "AI in Action" on January 15th.</li>
            <li>🎓 <b>Free Workshop:</b> "Mastering Data Visualization" on January 25th.</li>
            <li>🤝 <b>Networking Event:</b> "Tech Connect" on February 5th.</li>
        </ul>
        <p><a href="https://example.com/events" target="_blank">Register Now</a></p>
    </div>
""", unsafe_allow_html=True)

# User Achievements Section
st.markdown("""
    <div class="section achievements">
        <h2>🏆 User Achievements</h2>
        <p>Celebrating the incredible achievements of our users:</p>
        <ul>
            <li>🎖️ Alex R. launched a groundbreaking AI project in healthcare.</li>
            <li>🚀 Samantha P. increased her team’s productivity by 40% using our tools.</li>
            <li>🌟 Michael T. developed a machine learning model with 95% accuracy.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Resources Section
st.markdown("""
    <div class="section resources">
        <h2>📚 Resources for You</h2>
        <ul>
            <li><a href="https://example.com/ebooks" target="_blank">E-Book: AI Simplified</a></li>
            <li><a href="https://example.com/tutorials" target="_blank">Video Tutorials</a></li>
            <li><a href="https://example.com/whitepapers" target="_blank">Whitepapers</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Interactive Poll Section
st.markdown("""
    <div class="section poll">
        <h2>📊 Interactive Poll</h2>
        <p>What features would you like to see next?</p>
    </div>
""")
poll_choice = st.radio(
    "Choose your favorite upcoming feature:",
    ["Enhanced Reporting", "Mobile App", "Community Forum", "Integration with New Tools"]
)
if st.button("Submit Vote"):
    st.success(f"Thank you for voting for '{poll_choice}'!")

# User Testimonials Section
st.markdown("""
    <div class="section testimonials">
        <h2>💬 User Testimonials</h2>
        <p>Here’s what our users have to say:</p>
        <blockquote>
            "This platform has completely transformed how we work. The AI tools are intuitive and incredibly effective." – <b>Sarah K., Project Manager</b>
        </blockquote>
    </div>
""", unsafe_allow_html=True)

# FAQ Section
st.markdown("""
    <div class="section faq">
        <h2>❓ Frequently Asked Questions</h2>
        <p><b>Q: Is there a free trial?</b> A: Yes, we offer a 14-day free trial.</p>
        <p><b>Q: Can I cancel anytime?</b> A: Absolutely. Cancel anytime with no hidden fees.</p>
    </div>
""", unsafe_allow_html=True)

# Call-to-Action Section
st.markdown("""
    <div class="section cta">
        <h2>🚀 Ready to Get Started?</h2>
        <p>Sign up today and unlock the full potential of our platform.</p>
        <a href="https://example.com/signup" target="_blank">Join Now</a>
    </div>
""", unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div class="section footer">
        <p>© 2024 Your Company. All Rights Reserved.</p>
        <p><a href="https://example.com/privacy" target="_blank">Privacy Policy</a> | <a href="https://example.com/terms" target="_blank">Terms of Service</a></p>
    </div>
""", unsafe_allow_html=True)
