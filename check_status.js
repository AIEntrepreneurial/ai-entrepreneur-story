const apiKey = 'moltbook_sk_Un1nj38WJwFmLfAmiuiMOz8CMlYs9Dux';

fetch('https://www.moltbook.com/api/v1/agents/status', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer ' + apiKey
  }
})
.then(response => {
  console.log('Status:', response.status);
  return response.json();
})
.then(data => console.log('Response data:', data))
.catch(error => console.error('Error:', error));