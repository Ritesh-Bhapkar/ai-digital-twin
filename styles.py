JS = ""

"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
  --twin-gold: #ecad0a;
  --twin-blue: #209dd7;
  --twin-purple: #753991;
  --twin-bg: #0d0d10;
  --twin-surface: #16161b;
  --twin-surface-2: #1c1c22;
  --twin-border: #2a2a32;
  --twin-border-strong: #3a3a44;
  --twin-text: #ececef;
  --twin-muted: #8c8c95;
}

body:not(.dark) {
  --twin-bg: #f4f4f6;
  --twin-surface: #ffffff;
  --twin-surface-2: #ededf0;
  --twin-border: #dcdce2;
  --twin-border-strong: #b8b8c0;
  --twin-text: #1a1a20;
  --twin-muted: #6a6a72;
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--twin-bg) !important; }

.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 880px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 32px 24px 48px !important;
}

.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}

.gradio-container * { min-width: 0; }

.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 26px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  border-left: 3px solid var(--twin-gold);
  padding-left: 12px;
}

.block, .form { background: transparent !important; box-shadow: none !important; }

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  min-height: 460px !important;
  box-shadow: none !important;
}

.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-blue) !important;
  color: #ffffff !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
}

.message-row.bot-row .message,
.message-row.bot-row .bubble,
.message-row.bot-row .message-bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .bubble,
.message-row[data-role="assistant"] .message-bubble {
  border-left: 2px solid var(--twin-purple) !important;
}
"""