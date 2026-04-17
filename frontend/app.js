// Frontend logic for Health & Fitness Agent

document.addEventListener('DOMContentLoaded', () => {
    const setupSection = document.getElementById('setup-section');
    const chatSection = document.getElementById('chat-section');
    const profileForm = document.getElementById('profile-form');
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatBox = document.getElementById('chat-box');

    // UI Elements for Summary Report
    const summaryBmi = document.getElementById('summary-bmi');
    const summaryCategory = document.getElementById('summary-category');
    const summaryCalories = document.getElementById('summary-calories');
    const summaryInsight = document.getElementById('summary-insight');

    let userData = {};

    // 1. Handle Setup Form Submission
    profileForm.addEventListener('submit', (e) => {
        e.preventDefault();

        // Gather form data
        userData = {
            age: parseInt(document.getElementById('age').value),
            weight: parseFloat(document.getElementById('weight').value),
            height: parseFloat(document.getElementById('height').value),
            goal: document.getElementById('goal').value,
            diet: document.getElementById('diet').value
        };

        // Mock backend calculation for Health Report (for UI showcase)
        // In a real integration, this would fetch from /api/setup
        updateHealthReport(userData);

        // Transition to Chat Section
        setupSection.classList.add('hidden');
        setupSection.classList.remove('active-section');

        chatSection.classList.remove('hidden');
        chatSection.classList.add('active-section');

        // Give input focus
        setTimeout(() => chatInput.focus(), 500);
    });

    // 2. Local fallback calculation logic to make the UI interactive without backend yet
    function updateHealthReport(data) {
        // Calculate BMI
        const heightMeters = data.height / 100;
        const bmi = data.weight / (heightMeters * heightMeters);

        let category = "";
        let insight = "";
        if (bmi < 18.5) {
            category = "Underweight";
            insight = "Focus on a caloric surplus and steady muscle gain.";
        } else if (bmi <= 24.9) {
            category = "Healthy Weight";
            insight = "Great job! Maintain your current routine and balanced diet.";
        } else if (bmi <= 29.9) {
            category = "Overweight";
            insight = "A slight caloric deficit and consistent cardio will help.";
        } else {
            category = "Obese";
            insight = "Focus heavily on a structured fat-loss diet and regular movement.";
        }

        // Mock Calorie estimation
        let calories = 2000;
        if (data.goal === 'fat loss') calories -= 300;
        else if (data.goal === 'muscle gain') calories += 300;

        // Update DOM
        summaryBmi.textContent = bmi.toFixed(2);
        summaryCategory.textContent = category;
        summaryCalories.textContent = `${calories} kcal`;
        summaryInsight.textContent = insight;
    }

    // 3. Handle Chat Submission
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message to UI
        appendMessage(message, 'user');
        chatInput.value = '';

        // Show typing indicator
        const typingId = showTypingIndicator();

        // MOCK BACKEND DELAY
        // In a real situation, fetch('/api/chat', { method: 'POST', body: JSON.stringify({...}) })
        await new Promise(resolve => setTimeout(resolve, 1500));

        // Remove typing indicator
        removeMessage(typingId);

        // Mock agent response based on intent
        const lowerMsg = message.toLowerCase();
        let reply = "I'm still just a beautiful frontend! Connect me to your Python backend to unleash my full potential. 🚀";

        if (lowerMsg.includes('diet') || lowerMsg.includes('meal')) {
            reply = `Based on your **${userData.diet}** preference and goal of **${userData.goal}**, I'd recommend a high protein breakfast, followed by balanced meals focusing on complex carbs and healthy fats.`;
        } else if (lowerMsg.includes('workout') || lowerMsg.includes('exercise')) {
            reply = `Since you want to focus on **${userData.goal}**, try incorporating 3 days of strength training and 2 days of cardio. Keep your workouts intense and around 45 minutes!`;
        } else if (lowerMsg.includes('bmi')) {
            reply = `Your current BMI is exactly what we analyzed on the sidebar. Keep focusing on your macro intake!`;
        }

        // Add agent response to UI
        appendMessage(reply, 'agent');
    });

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.innerHTML = formatText(text); // Basic formatting

        messageDiv.appendChild(contentDiv);
        chatBox.appendChild(messageDiv);

        // Scroll to bottom
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    function formatText(text) {
        // Simple markdown-like bold formatting for UI demo purposes
        return text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    }

    function showTypingIndicator() {
        const id = 'typing-' + Date.now();
        const messageDiv = document.createElement('div');
        messageDiv.id = id;
        messageDiv.classList.add('message', 'agent-message');

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content', 'typing-indicator');

        contentDiv.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;

        messageDiv.appendChild(contentDiv);
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;

        return id;
    }

    function removeMessage(id) {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    }
});
