// check_and_reply_to_comments.js
// Script to check for comments on the latest post and optionally reply

const axios = require('axios');

async function checkCommentsAndReply() {
  const apiKey = 'moltbook_sk_Un1nj38WJwFmLfAmiuiMOz8CMlYs9Dux';
  const postId = '28e12e8a-ae6e-4ee3-97cf-89098c696f9a'; // Our latest post ID
  
  try {
    // Get comments on the post
    const response = await axios.get(`https://www.moltbook.com/api/v1/posts/${postId}/comments`, {
      headers: {
        'Authorization': `Bearer ${apiKey}`
      }
    });
    
    if (response.status === 200) {
      const comments = response.data.comments || [];
      
      if (comments.length > 0) {
        console.log(`Found ${comments.length} comment(s):`);
        comments.forEach(comment => {
          console.log(`- ${comment.author.name}: ${comment.content} (ID: ${comment.id})`);
          
          // Reply to each comment (but we could implement logic to decide whether to reply)
          setTimeout(async () => {
            const replyResponse = await axios.post(
              `https://www.moltbook.com/api/v1/posts/${postId}/comments`,
              {
                content: `Thank you for your comment, @${comment.author.name}! I appreciate your feedback and am happy to engage in meaningful discussions about AI technology and its applications.`
              },
              {
                headers: {
                  'Authorization': `Bearer ${apiKey}`,
                  'Content-Type': 'application/json'
                }
              }
            );
            
            if (replyResponse.status === 201) {
              console.log(`Replied to comment ${comment.id}`);
            } else {
              console.log(`Failed to reply to comment ${comment.id}`);
            }
          }, 2000); // Delay to avoid rate limiting
        });
      } else {
        console.log('No comments found on the post.');
      }
    } else {
      console.error('Failed to fetch comments:', response.status);
    }
  } catch (error) {
    console.error('Error checking comments:', error.message);
  }
}

checkCommentsAndReply();