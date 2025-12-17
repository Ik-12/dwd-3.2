# Url-shortener demo

The service is available at https://url-shortener-gtje.onrender.com/shorten

## Usage

### Get shortened url

```
curl -X POST https://url-shortener-gtje.onrender.com/shorten \
     -H "Content-Type: application/json" \
     -d '{"url":"https://www.python.org"}'
```
