# ADHI AI

Advanced Intelligent Assistant - A simple AI chat application with Vercel Web Analytics integration.

## Features

- 🤖 Interactive AI chat interface
- 📊 Vercel Web Analytics for tracking visitors and page views
- 🎨 Modern, responsive design
- ⚡ Fast and lightweight
- 🔒 Privacy-compliant analytics

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- A Vercel account (for analytics features)

### Local Development

1. Clone this repository:
```bash
git clone https://github.com/sankarankundi/adhi-ai.git
cd adhi-ai
```

2. Run the local server:
```bash
python3 script47.py
```

3. Open your browser and navigate to:
```
http://localhost:8000
```

The chat interface will be available, and you can start interacting with ADHI AI.

## Vercel Web Analytics

This project includes Vercel Web Analytics integration for tracking user interactions and page views.

### Setup Web Analytics on Vercel

1. **Enable Web Analytics in Vercel Dashboard**
   - Go to your [Vercel dashboard](https://vercel.com/dashboard)
   - Select your project
   - Click the **Analytics** tab
   - Click **Enable** to activate Web Analytics

2. **Deploy to Vercel**
   ```bash
   vercel deploy
   ```

3. **Verify Integration**
   - After deployment, visit your site
   - Open browser Developer Tools > Network tab
   - Look for a request to `/_vercel/insights/view`
   - If you see this request, analytics is working correctly!

### Analytics Implementation

This project uses the HTML implementation of Vercel Web Analytics, which is included in the `<head>` section of `index.html`:

```html
<!-- Vercel Web Analytics -->
<script>
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

**Note:** No package installation is required for the HTML implementation. The analytics script is automatically served by Vercel after deployment.

### Viewing Analytics Data

Once deployed and receiving traffic:
1. Go to your [Vercel dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click the **Analytics** tab
4. View visitor data, page views, and other metrics

## Project Structure

```
adhi-ai/
├── index.html       # Main chat interface with Vercel Analytics
├── script47.py      # Python HTTP server with chat API
└── README.md        # This file
```

## API Endpoints

### POST /api/chat

Send a message to ADHI AI and receive a response.

**Request:**
```json
{
  "message": "Hello, ADHI!"
}
```

**Response:**
```json
{
  "reply": "Hello! I am ADHI AI. How can I assist you today?"
}
```

## Privacy & Compliance

Vercel Web Analytics is privacy-friendly and compliant with GDPR, CCPA, and other privacy regulations. It does not use cookies and does not track personal information. Learn more about [Vercel's privacy policy](https://vercel.com/docs/analytics/privacy-policy).

## Next Steps

- [Learn more about Vercel Analytics](https://vercel.com/docs/analytics)
- [Set up custom events](https://vercel.com/docs/analytics/custom-events)
- [Explore data filtering](https://vercel.com/docs/analytics/filtering)
- [View pricing and limits](https://vercel.com/docs/analytics/limits-and-pricing)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
