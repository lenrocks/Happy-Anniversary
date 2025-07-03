import streamlit as st
import random
import time

st.set_page_config(page_title="Anniversary Game 🎉", page_icon="💖", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        color: #FF69B4;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px #FF69B4, 0 0 40px #FF1493;
        animation: pulse-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes pulse-glow {
        from { text-shadow: 0 0 20px #FF69B4, 0 0 40px #FF1493; }
        to { text-shadow: 0 0 30px #FF69B4, 0 0 60px #FF1493, 0 0 80px #FF69B4; }
    }
    
    /* Animated background */
    .stApp {
        background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #533483);
        background-size: 400% 400%;
        animation: gradient-shift 15s ease infinite;
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Level 1 - Basketball Court Theme */
    .level1-bg {
        background: linear-gradient(135deg, #ff6b35, #f7931e, #ffcc02);
        position: relative;
        overflow: hidden;
    }
    
    .level1-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="2" fill="rgba(255,255,255,0.1)"/></svg>');
        background-size: 50px 50px;
        animation: float-dots 20s linear infinite;
    }
    
    @keyframes float-dots {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-100px); }
    }
    
    /* Level 2 - Heart Matrix */
    .level2-bg {
        background: linear-gradient(45deg, #ff0844, #ff6b9d, #c44569);
        position: relative;
    }
    
    .heart-matrix {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden;
    }
    
    .heart-particle {
        position: absolute;
        color: rgba(255, 255, 255, 0.1);
        font-size: 20px;
        animation: heart-fall 8s linear infinite;
    }
    
    @keyframes heart-fall {
        0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    
    /* Level 3 - Time Warp */
    .level3-bg {
        background: linear-gradient(45deg, #667eea, #764ba2, #f093fb);
        position: relative;
    }
    
    .time-spiral {
        position: absolute;
        width: 200px;
        height: 200px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        animation: spiral-rotate 10s linear infinite;
    }
    
    @keyframes spiral-rotate {
        0% { transform: translate(-50%, -50%) rotate(0deg) scale(1); }
        50% { transform: translate(-50%, -50%) rotate(180deg) scale(1.2); }
        100% { transform: translate(-50%, -50%) rotate(360deg) scale(1); }
    }
    
    /* Level 4 - Gaming Neon */
    .level4-bg {
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb, #4facfe);
        position: relative;
    }
    
    .neon-grid {
        position: absolute;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(0, 255, 255, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 255, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: grid-glow 3s ease-in-out infinite alternate;
    }
    
    @keyframes grid-glow {
        0% { opacity: 0.3; }
        100% { opacity: 0.8; }
    }
    
    /* Level 5 - Ocean Waves */
    .level5-bg {
        background: linear-gradient(135deg, #667eea, #764ba2, #4facfe, #00f2fe);
        position: relative;
    }
    
    .wave {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 100px;
        background: linear-gradient(45deg, rgba(0, 242, 254, 0.3), rgba(111, 172, 234, 0.3));
        border-radius: 50px 50px 0 0;
        animation: wave-motion 4s ease-in-out infinite;
    }
    
    @keyframes wave-motion {
        0%, 100% { transform: translateX(0px); }
        50% { transform: translateX(-20px); }
    }
    
    /* Celebration - Fireworks */
    .celebration-bg {
        background: radial-gradient(circle at 20% 50%, #ff6b35, transparent 50%),
                    radial-gradient(circle at 80% 20%, #f7931e, transparent 50%),
                    radial-gradient(circle at 40% 80%, #ffcc02, transparent 50%),
                    radial-gradient(circle at 60% 30%, #ff0844, transparent 50%),
                    linear-gradient(135deg, #1a1a2e, #16213e);
        animation: fireworks 3s ease-in-out infinite;
    }
    
    @keyframes fireworks {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.5); }
    }
    
    .level-progress {
        background: linear-gradient(90deg, #FF1493, #FF69B4, #FFB6C1);
        height: 15px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 0 20px rgba(255, 105, 180, 0.5);
        animation: progress-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes progress-glow {
        0% { box-shadow: 0 0 20px rgba(255, 105, 180, 0.5); }
        100% { box-shadow: 0 0 30px rgba(255, 105, 180, 0.8); }
    }
    
    .love-note {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .game-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
    }
    
    /* Floating elements */
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }
    
    .floating-heart {
        position: absolute;
        animation: float-up 4s linear infinite;
        font-size: 30px;
        filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.8));
    }
    
    @keyframes float-up {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
    }
    
    /* Particle effects */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }
    
    .particle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 50%;
        animation: particle-float 15s linear infinite;
    }
    
    @keyframes particle-float {
        0% { transform: translateY(100vh) translateX(0px); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) translateX(100px); opacity: 0; }
    }
    
    .confetti {
        position: fixed;
        top: -10px;
        z-index: 9999;
        pointer-events: none;
    }
    
    @keyframes confetti-fall {
        0% { transform: translateY(-100vh) rotate(0deg); }
        100% { transform: translateY(100vh) rotate(720deg); }
    }
    
    .voice-note-container {
        background: linear-gradient(135deg, rgba(255, 182, 193, 0.3), rgba(255, 192, 203, 0.3));
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 105, 180, 0.3);
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(255, 105, 180, 0.2);
        animation: voice-note-glow 3s ease-in-out infinite alternate;
    }
    
    @keyframes voice-note-glow {
        0% { box-shadow: 0 8px 32px rgba(255, 105, 180, 0.2); }
        100% { box-shadow: 0 8px 32px rgba(255, 105, 180, 0.4); }
    }
    
    /* Button animations */
    .stButton > button {
        background: linear-gradient(45deg, #ff6b35, #f7931e) !important;
        border: none !important;
        color: white !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(255, 107, 53, 0.5) !important;
    }
    
    /* Level-specific backgrounds */
    .level1 { background: linear-gradient(135deg, #ff6b35, #f7931e, #ffcc02); }
    .level2 { background: linear-gradient(45deg, #ff0844, #ff6b9d, #c44569); }
    .level3 { background: linear-gradient(45deg, #667eea, #764ba2, #f093fb); }
    .level4 { background: linear-gradient(135deg, #667eea, #764ba2, #f093fb, #4facfe); }
    .level5 { background: linear-gradient(135deg, #667eea, #764ba2, #4facfe, #00f2fe); }
    .celebration { background: radial-gradient(circle at 20% 50%, #ff6b35, transparent 50%), radial-gradient(circle at 80% 20%, #f7931e, transparent 50%), radial-gradient(circle at 40% 80%, #ffcc02, transparent 50%), radial-gradient(circle at 60% 30%, #ff0844, transparent 50%), linear-gradient(135deg, #1a1a2e, #16213e); }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'level' not in st.session_state:
    st.session_state.level = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'hints_used' not in st.session_state:
    st.session_state.hints_used = 0
if 'secret_found' not in st.session_state:
    st.session_state.secret_found = False
if 'show_floating_hearts' not in st.session_state:
    st.session_state.show_floating_hearts = False

# Add particles background
def add_particles():
    st.markdown("""
    <div class="particles">
        <div class="particle" style="left: 10%; animation-delay: 0s;"></div>
        <div class="particle" style="left: 20%; animation-delay: 2s;"></div>
        <div class="particle" style="left: 30%; animation-delay: 4s;"></div>
        <div class="particle" style="left: 40%; animation-delay: 6s;"></div>
        <div class="particle" style="left: 50%; animation-delay: 8s;"></div>
        <div class="particle" style="left: 60%; animation-delay: 10s;"></div>
        <div class="particle" style="left: 70%; animation-delay: 12s;"></div>
        <div class="particle" style="left: 80%; animation-delay: 14s;"></div>
        <div class="particle" style="left: 90%; animation-delay: 16s;"></div>
    </div>
    """, unsafe_allow_html=True)

# Level-specific background effects
def add_level_background(level):
    if level == 1:
        st.markdown('<div class="level1-bg"></div>', unsafe_allow_html=True)
    elif level == 2:
        st.markdown("""
        <div class="heart-matrix">
            <div class="heart-particle" style="left: 10%; animation-delay: 0s;">💖</div>
            <div class="heart-particle" style="left: 20%; animation-delay: 1s;">💕</div>
            <div class="heart-particle" style="left: 30%; animation-delay: 2s;">💘</div>
            <div class="heart-particle" style="left: 40%; animation-delay: 3s;">💝</div>
            <div class="heart-particle" style="left: 50%; animation-delay: 4s;">💗</div>
            <div class="heart-particle" style="left: 60%; animation-delay: 5s;">💖</div>
            <div class="heart-particle" style="left: 70%; animation-delay: 6s;">💕</div>
            <div class="heart-particle" style="left: 80%; animation-delay: 7s;">💘</div>
            <div class="heart-particle" style="left: 90%; animation-delay: 8s;">💝</div>
        </div>
        """, unsafe_allow_html=True)
    elif level == 3:
        st.markdown('<div class="time-spiral"></div>', unsafe_allow_html=True)
    elif level == 4:
        st.markdown('<div class="neon-grid"></div>', unsafe_allow_html=True)
    elif level == 5:
        st.markdown('<div class="wave"></div>', unsafe_allow_html=True)
    elif level == 6:
        st.markdown('<div class="celebration-bg"></div>', unsafe_allow_html=True)
# Animation functions
def trigger_floating_hearts():
    st.session_state.show_floating_hearts = True
    st.markdown("""
    <div class="floating-hearts">
        <div class="floating-heart" style="left: 10%; animation-delay: 0s;">💖</div>
        <div class="floating-heart" style="left: 20%; animation-delay: 0.5s;">💕</div>
        <div class="floating-heart" style="left: 30%; animation-delay: 1s;">💘</div>
        <div class="floating-heart" style="left: 40%; animation-delay: 1.5s;">💝</div>
        <div class="floating-heart" style="left: 50%; animation-delay: 2s;">💗</div>
        <div class="floating-heart" style="left: 60%; animation-delay: 2.5s;">💖</div>
        <div class="floating-heart" style="left: 70%; animation-delay: 3s;">💕</div>
        <div class="floating-heart" style="left: 80%; animation-delay: 3.5s;">💘</div>
        <div class="floating-heart" style="left: 90%; animation-delay: 4s;">💝</div>
    </div>
    """, unsafe_allow_html=True)

def show_confetti():
    st.markdown("""
    <div class="confetti">
        <div style="position: fixed; top: -10px; left: 10%; animation: confetti-fall 3s linear; color: #FF69B4;">🎉</div>
        <div style="position: fixed; top: -10px; left: 20%; animation: confetti-fall 3s linear 0.2s; color: #FFB6C1;">🎊</div>
        <div style="position: fixed; top: -10px; left: 30%; animation: confetti-fall 3s linear 0.4s; color: #FF1493;">✨</div>
        <div style="position: fixed; top: -10px; left: 40%; animation: confetti-fall 3s linear 0.6s; color: #FFC0CB;">🌟</div>
        <div style="position: fixed; top: -10px; left: 50%; animation: confetti-fall 3s linear 0.8s; color: #FF69B4;">🎉</div>
        <div style="position: fixed; top: -10px; left: 60%; animation: confetti-fall 3s linear 1s; color: #FFB6C1;">🎊</div>
        <div style="position: fixed; top: -10px; left: 70%; animation: confetti-fall 3s linear 1.2s; color: #FF1493;">✨</div>
        <div style="position: fixed; top: -10px; left: 80%; animation: confetti-fall 3s linear 1.4s; color: #FFC0CB;">🌟</div>
        <div style="position: fixed; top: -10px; left: 90%; animation: confetti-fall 3s linear 1.6s; color: #FF69B4;">🎉</div>
    </div>
    """, unsafe_allow_html=True)

def add_voice_note(level_num, message):
    st.markdown(f"""
    <div class="voice-note-container">
        <h4>🎧 Audio Message Unlocked 🎧</h4>
        <p style="font-style: italic; color: #8B0000;">{message}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add audio player with correct file path
    try:
        if level_num == 1:
            st.audio("Level 1.m4a")
        elif level_num == 2:
            st.audio("Level 2.m4a")
        elif level_num == 3:
            st.audio("Level 3.m4a")
        elif level_num == 5:
            st.audio("Level 5.m4a")
        elif level_num == "CALENDAR SECRET":
            st.audio("Celebratory note.m4a")
        elif level_num == "FINAL":
            st.audio("Final note.m4a")
        else:
            st.write("💡 Voice note placeholder - add your .m4a file!")
    except Exception as e:
        st.error(f"Audio file error: {e}")
        st.write(f"Looking for file: {level_num}")

# Progress bar
def show_progress():
    progress = min(st.session_state.level / 5, 1.0)  # Cap at 1.0 for levels 1-5
    st.progress(progress)
    st.write(f"Progress: Level {st.session_state.level}/5 {'🏆' if st.session_state.level >= 6 else ''}")

# Hint system
def show_hint(level_num, hint_text):
    if st.button(f"💡 Need a hint for Level {level_num}?", key=f"hint_{level_num}"):
        st.info(f"💡 Hint: {hint_text}")
        st.session_state.hints_used += 1
        # Don't return anything - just display the hint

# Track attempts
def track_attempt(level_num):
    if level_num not in st.session_state.attempts:
        st.session_state.attempts[level_num] = 0
    st.session_state.attempts[level_num] += 1

# Enhanced level functions
def level_1():
    add_level_background(1)
    st.markdown('<div class="game-card level1">', unsafe_allow_html=True)
    st.subheader("🏀 Level 1: Where It All Began")
    st.write("Let's start with where our love story began...")
    
    ans = st.text_input("Where did we first meet?", placeholder="Type your answer here...")
    
    if ans.lower().strip() == "monmouth basketball court":
        st.success("Correct! 🎉 Our first meeting at the basketball court!")
        st.balloons()
        trigger_floating_hearts()
        show_confetti()
        add_voice_note(1, "Nailed it! First try too... okay maybe not ? prolly not.  🏀")
        
        # Add continue button
        if st.button("✨ Continue to Level 2!", key="continue_1", use_container_width=True):
            return True
        
    elif ans:
        track_attempt(1)
        st.warning("Try again! Think about sports... 🏀")
        show_hint(1, "It's a place where people play a sport with hoops!")
    
    # Easter egg - separate from the main answer logic
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🏀", help="Secret!", key="secret_1"):
            st.success("🎉 SECRET FOUND! You found the hidden basketball!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def level_2():
    add_level_background(2)
    st.markdown('<div class="game-card level2">', unsafe_allow_html=True)
    st.subheader("💘 Level 2: Find My Heart")
    st.write("Among all these hearts, find the one that represents our love!")
    
    # Create a consistent set of hearts for this session
    if 'level2_hearts' not in st.session_state:
        hearts = ["💔", "💖", "💔"]
        random.shuffle(hearts)
        st.session_state.level2_hearts = hearts
    
    # Check if correct heart was found
    if 'level2_correct' not in st.session_state:
        st.session_state.level2_correct = False
    
    # If already found correct heart, show continue button
    if st.session_state.level2_correct:
        st.success("You found our special heart! 💘")
        st.balloons()
        trigger_floating_hearts()
        show_confetti()
        add_voice_note(2, "You found the right heart 💖")
        
        if st.button("✨ Continue to Level 3!", key="continue_2", use_container_width=True):
            # Clear the hearts and correct flag for next time
            if 'level2_hearts' in st.session_state:
                del st.session_state.level2_hearts
            st.session_state.level2_correct = False
            return True
    else:
        # Show heart buttons
        cols = st.columns(3)
        for i, heart in enumerate(st.session_state.level2_hearts):
            with cols[i]:
                if st.button(heart, key=f"heart_{i}_{heart}"):
                    if heart == "💖":
                        st.session_state.level2_correct = True
                        st.rerun()
                    else:
                        track_attempt(2)
                        st.warning("That's not the right one! Try again! 💕")
                        # Reshuffle hearts after wrong answer
                        hearts = ["💔", "💖", "💔"]
                        random.shuffle(hearts)
                        st.session_state.level2_hearts = hearts
                        st.rerun()
        
        show_hint(2, "Look for the pink heart that sparkles with our love!")
    
    # Easter egg - hidden in the corner
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col3:
        if st.button(".", help="What's this tiny dot?", key="secret_2"):
            st.success("🎊 EASTER EGG! You found the secret dot!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def level_3():
    add_level_background(3)
    st.markdown('<div class="game-card level3">', unsafe_allow_html=True)
    st.subheader("📅 Level 3: Anniversary Memory")
    st.write("Before we settled on our perfect date, what was our original anniversary?")
    
    ans = st.text_input("What was our original anniversary date before we changed it?", 
                       placeholder="MM/DD format")
    
    if ans.strip() == "09/11":
        st.success("Yes! We decided to change it to something more special! 💕")
        st.balloons()
        trigger_floating_hearts()
        add_voice_note(3, "Do you remember when I basically forced you to ask me? lol ")
        
        # Add continue button
        if st.button("✨ Continue to Level 4!", key="continue_3", use_container_width=True):
            return True
            
    elif ans:
        track_attempt(3)
        st.warning("Hmm, not quite. Think about a significant date in history...")
        show_hint(3, "It's a date that's remembered for other reasons in history...")
    
    # Show hint if no answer yet
    if not ans:
        show_hint(3, "It's a date that's remembered for other reasons in history...")
    
    # Easter egg - hidden calendar
    st.markdown("---")
    if st.button("📅 What's today's date?", key="secret_3"):
        st.success("🎉 SURPRISE! Today's date is special because it's our anniversary!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def level_4():
    add_level_background(4)
    st.markdown('<div class="game-card level4">', unsafe_allow_html=True)
    st.subheader("🎮 Level 4: Mini Flappy Bird Game")
    st.write("Time to play some Flappy Bird! Navigate the bird through the pipes!")
    
    # Initialize game state
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'bird_position' not in st.session_state:
        st.session_state.bird_position = 50
    if 'game_score' not in st.session_state:
        st.session_state.game_score = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'pipes' not in st.session_state:
        st.session_state.pipes = [70, 30, 80, 25, 75]
    
    # Game display
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if not st.session_state.game_started:
            st.write("🕊️ **Flappy Bird Anniversary Edition**")
            st.write("Click 'Flap!' to make the bird fly up, avoid the pipes!")
            if st.button("🚀 Start Game", use_container_width=True):
                st.session_state.game_started = True
                st.session_state.game_over = False
                st.session_state.bird_position = 50
                st.session_state.game_score = 0
                st.rerun()
        
        elif not st.session_state.game_over:
            # Game area visualization
            st.write(f"**Score: {st.session_state.game_score}** 🏆")
            
            # Simple visual representation
            game_area = ""
            for i in range(10):
                if i == int(st.session_state.bird_position / 10):
                    game_area += "🕊️ ← Bird position\n"
                elif i in [2, 7]:  # Pipe positions
                    game_area += "🟫🟫🟫 ← Pipes\n"
                else:
                    game_area += "🌤️ \n"
            
            st.text(game_area)
            
            # Game controls
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("🕊️ Flap!", use_container_width=True):
                    st.session_state.bird_position = max(0, st.session_state.bird_position - 20)
                    st.session_state.game_score += 1
                    
                    # Simple collision detection
                    if st.session_state.bird_position in [20, 70]:  # Hit pipes
                        st.session_state.game_over = True
                        st.warning("💥 You hit a pipe!")
                    elif st.session_state.bird_position <= 0 or st.session_state.bird_position >= 90:
                        st.session_state.game_over = True
                        st.warning("💥 You crashed!")
                    else:
                        st.success("Good flap! 🕊️")
                    st.rerun()
            
            with col_b:
                if st.button("⬇️ Drop", use_container_width=True):
                    st.session_state.bird_position = min(90, st.session_state.bird_position + 15)
                    
                    # Simple collision detection
                    if st.session_state.bird_position in [20, 70]:  # Hit pipes
                        st.session_state.game_over = True
                        st.warning("💥 You hit a pipe!")
                    elif st.session_state.bird_position <= 0 or st.session_state.bird_position >= 90:
                        st.session_state.game_over = True
                        st.warning("💥 You crashed!")
                    st.rerun()
            
            with col_c:
                if st.button("🔄 Reset", use_container_width=True):
                    st.session_state.game_started = False
                    st.session_state.bird_position = 50
                    st.session_state.game_score = 0
                    st.session_state.game_over = False
                    st.rerun()
        
        else:  # Game over
            st.write(f"**Game Over! Final Score: {st.session_state.game_score}** 🏁")
            
            if st.session_state.game_score >= 5:
                st.success("🎉 Amazing! You scored enough to continue!")
                if st.button("✅ Continue to Next Level", use_container_width=True):
                    return True
            else:
                st.warning(f"You need at least 5 points to continue. You scored: {st.session_state.game_score}")
                show_hint(4, "Try to flap more carefully and avoid the pipes!")
            
            if st.button("🔄 Play Again", use_container_width=True):
                st.session_state.game_started = False
                st.session_state.bird_position = 50
                st.session_state.game_score = 0
                st.session_state.game_over = False
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def level_5():
    add_level_background(5)
    st.markdown('<div class="game-card level5">', unsafe_allow_html=True)
    st.subheader("🏖️ Level 5: First Date Memory")
    st.write("Our very first official date... where did we go to start this beautiful journey?")
    
    ans = st.text_input("Where was our first date?", placeholder="Think about sand and waves...")
    
    if ans.lower().strip() == "beach":
        st.success("YES! Our romantic beach date! 🏖️💕")
        st.balloons()
        trigger_floating_hearts()
        show_confetti()
        add_voice_note(5, "I remember being soo nervous and picking the 'coolest but not try hard outfit'")
        
        # Add continue button
        if st.button("✨ Continue to Bonus Level!", key="continue_5", use_container_width=True):
            return True
            
    elif ans:
        track_attempt(5)
        st.warning("Not quite! Think about somewhere peaceful with water...")
        # Don't show hint for beach answer
    
    # Final easter egg
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("🌊", help="Ocean sounds?", key="secret_5"):
            st.success("🏖️ FINAL SECRET! You found the ocean!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def bonus_level():
    add_level_background(6)
    st.markdown('<div class="game-card celebration">', unsafe_allow_html=True)
    st.subheader("🎉 VICTORY CELEBRATION! 🎉")
    st.write("You made it through all 5 levels! Time to celebrate our love! 💕")
    
    # Automatic celebrations
    st.balloons()
    trigger_floating_hearts()
    show_confetti()
    
    # Fun interactive celebration buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🎊 MORE CONFETTI!", use_container_width=True):
            st.balloons()
            show_confetti()
            st.success("🎊 WOOHOO! Confetti everywhere!")
    
    with col2:
        if st.button("💕 HEART EXPLOSION!", use_container_width=True):
            trigger_floating_hearts()
            st.success("💖 Hearts are flying! Just like my heart for you!")
    
    with col3:
        if st.button("🌟 SPARKLE MAGIC!", use_container_width=True):
            st.balloons()
            st.success("✨ You're sparkling like the star you are!")
    
    # Victory messages
    victory_messages = [
        "🏆 Anniversary Game Champion unlocked!",
        "💝 Three years down, infinity to go!",
        "🎮 You beat my game AND my heart!",
        "🌟 Gaming skills: 10/10, Being my person: 11/10",
        "💕 This celebration is pretty cool but you're cooler"
    ]
    
    # Cycling celebration messages
    if 'celebration_msg_index' not in st.session_state:
        st.session_state.celebration_msg_index = 0
    
    if st.button("🎯 GET VICTORY MESSAGE!", use_container_width=True):
        st.success(victory_messages[st.session_state.celebration_msg_index])
        st.session_state.celebration_msg_index = (st.session_state.celebration_msg_index + 1) % len(victory_messages)
        trigger_floating_hearts()
    
    # Dance party section
    st.markdown("---")
    st.write("🕺💃 **VIRTUAL DANCE PARTY TIME!** 💃🕺")
    
    dance_col1, dance_col2 = st.columns(2)
    with dance_col1:
        if st.button("🎵 DANCE MOVE 1!", use_container_width=True):
            st.write("💃 *spins around* 💃")
            st.balloons()
    
    with dance_col2:
        if st.button("🎵 DANCE MOVE 2!", use_container_width=True):
            st.write("🕺 *does the robot* 🕺")
            show_confetti()
    
    # Celebration voice note
    st.markdown("---")
    add_voice_note("CALENDAR SECRET", "These are kinda fun so go ahead and press every button!! 🎉")
    
    # Big continue button
    st.markdown("---")
    if st.button("🏆 READY FOR YOUR FINAL SURPRISE! 🏆", use_container_width=True):
        return True
    
    st.markdown('</div>', unsafe_allow_html=True)
    return False

def final_message():
    st.balloons()
    show_confetti()
    trigger_floating_hearts()
    
    # Calculate some fun stats
    total_time = int(time.time() - st.session_state.start_time)
    total_attempts = sum(st.session_state.attempts.values())
    
    st.markdown('<div class="love-note">', unsafe_allow_html=True)
    st.markdown("# 💌 A Love Letter Just For You 💌")
    
    st.markdown(f"""
    **My Dearest Klem,**
    
    🎉 **YOU DID IT!** 🎉
    
    You conquered all the levels and made it to the end! 
    
    **Your Gaming Stats:**
    - ⏱️ Time taken: {total_time // 60} minutes and {total_time % 60} seconds
    - 🎯 Total attempts: {total_attempts}
    - 💡 Hints used: {st.session_state.hints_used}
    - 🏆 Status: **ANNIVERSARY CHAMPION!**
    
    **Happy Anniversary, my sweetheart!** 💕
    
    Congrats bug!!! You did it!! Coding is hard, AI makes it easier but this took me HOURS so I hope you appreciate it! 
    
    Ok now for the real deal: Happy anniversary baby! I love you and I am so proud of us!! We are strong and only getting stronger! You are such a ray of light in my life and I genuinely am so so grateful to get to be yours and to experience life with you. But more importantly, I am so so so EXCITED for our life together!! There really isn't much to say that hasn't already been said but just wanna express my genuine, heartfelt love for you. Be nice to me, please. All I want is for us to be so in love and happy and having fun always! Nothing & nobody else matters! 
    
    Also, wtf? We've been dating for three full years?? Feels like forever. I feel like I have known you my whole life. Buuuut anyway. Happy anniversary, sweetheart. I love you endlessly.
    
    **All my love,**  
    **Your Player 2** 🎮💖
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Final voice message
    add_voice_note("FINAL", "You made it through my chaotic coding project! Happy anniversary bug! 💕")
    
    # Add some final interactive elements
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Want to play again?", use_container_width=True):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()
    
    with col2:
        if st.button("💝 One More Secret?", use_container_width=True):
            st.success("🎊 ULTIMATE SECRET UNLOCKED!")
            st.write("🤫 You found the final easter egg! You're so thorough! 😄")

# Main game flow
st.markdown('<h1 class="main-title">💘 Anniversary Game Adventure 💘</h1>', unsafe_allow_html=True)

# Show GIF only at start
if st.session_state.level == 0:
    st.image("https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif", use_container_width=True)
    st.markdown('<div class="love-note">', unsafe_allow_html=True)
    st.write("Welcome to our special anniversary game! Think you remember all our relationship milestones? Let's see what you got 💕")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 Let's Start This Adventure!", use_container_width=True):
        st.session_state.level = 1
        st.session_state.start_time = time.time()
        st.rerun()
else:
    show_progress()
    add_particles()  # Add floating particles to all levels

# Level routing
if st.session_state.level == 1:
    if level_1():
        st.session_state.level = 2
        st.rerun()
elif st.session_state.level == 2:
    if level_2():
        st.session_state.level = 3
        st.rerun()
elif st.session_state.level == 3:
    if level_3():
        st.session_state.level = 4
        st.rerun()
elif st.session_state.level == 4:
    if level_4():
        st.session_state.level = 5
        st.rerun()
elif st.session_state.level == 5:
    if level_5():
        st.session_state.level = 6
        st.rerun()
elif st.session_state.level == 6:
    if bonus_level():
        st.session_state.level = 7
        st.rerun()
elif st.session_state.level == 7:
    final_message()

# Footer
st.markdown("---")
st.markdown("*Made with 💖 for the most special person in the world*")