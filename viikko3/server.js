const express = require('express');
const app = express();
const port = 3000;
const sqlite3 = require('sqlite3');

app.use(express.json())

const db = new (require('sqlite3')).Database('./Severidatabase.db', (err) => {
    if (err) return console.error(err.message);
    console.log('Connected Sqlite database); 
}); 

db.run(`CREATE TABLE IF NOT EXIST users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
    )`);

// GET endpoint
app.get('/api/sensor', (req, res) => {
    res.json({
        temperature: 22.5,
        humidity: 55,
        status: "OK"
  });
});

app.get('/api/users', (req, res) => {
   console.log("In get endpoint");
   db.all('SELECT * FROM users', [], (err, rows) => {
        if (err) return res.status(500).json({error: err.message});
        res.json(rows);
    })
          
});

app.post('/api/users', (req, res) => {
    console.log("In post endpoint");
    const{ name, email } = req.body;
    db.run(`INSERT INTO users (name, email) VALUES (?, ?)`, [name, email], function(err){
        if (err) return res.status(400).json({error: error.message})
        res.status(201).json({id: this.lastID, name, email})
    })
    
});


app.listen(port, () => {
console.log(`Server running at http://localhost:${port}`);
});