import { error } from 'console';
import express from 'express';

const app = express();

const PORT = 3000;

const DISCORD_WEBHOOK_URL = 'https:https://discord.com/api/webhooks/1422173095879507969/vQQ_ksXiJe_mSFKglShgpuzaATHC7zKMErb2a8P5h2xIr5-OQ9oLkvYLgMrcHVGzDGtH';

app.use(express.json());

app.post('/notify', (req, res) => {
    const {message} = req.body;

    if(!message){
        return res.status(400).json({error: 'Message is required'})
    }
    fetch(DISCORD_WEBHOOK_URL, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({content:message})   
        
    }) 
    .then(response => {
        if(!response.ok){
            throw new Error(`Discord responded with statu ${response.status}`);
        }
       res.json({status: 'Message sent...'})
    }) 
    .catch(error =>{
        consoler.error('Error sending to Discord, error');
        res.status(500).json({error: 'Failed sending your message'});
    })

    
})

app.listen(PORT, () => {
    console.log(`Server running on localhost ${PORT}`);
})