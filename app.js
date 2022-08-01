const express = require('express');
const { exec } = require('child_process');
const fs = require('fs');
const app = express();
const port = 443;
const blender = '/opt/blender'

app.get('/', (req, res) => {
    
    var id = req.params['id'];
    var path = "./output/" + id + ".glb"
    
  if(fs.existsSync(path))
  {
    res.sendFile(path);
  } else
  {
    exec(blender + " -b -P run.py ./input/template.blend " + id, {},
        function() {
            res.sendFile(path);
        }
    );
  }
    
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
});
