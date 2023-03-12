import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';


function App() {
  
  const [selectedFile, setSelectedFile] = useState();
  const onFileChange = event => setSelectedFile(event.target.files[0]);
  const onFileUpload = () => {
    const formData = new FormData();
    formData.append(
          "myFile",
          selectedFile,
          this.state.selectedFile.name
        );
  }
  

  return (
    <div>
    

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>

    <div class="navbar">
      <a href="#"><i></i>Colour Palette</a>
      <a href="#"><i class="fa"></i> Upload</a>
      <a href="#"><i class="active"></i> Home</a>
      
    </div>

    <div className="App">
  
      <header className="App-header">
        
        <p>
          Welcome!
        </p>
        <div>
          <input type="file" onChange={onFileChange} />
          <button className="button" onClick={onFileUpload}>
            Upload!
          </button>
        </div>
        
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"></link>
        <p>Custom file:</p>
        <div class="custom-file mb-3">
          <input type="file" class="custom-file-input" id="customFile" name="filename"/>
          <label class="custom-file-label" for="customFile">Choose file</label>
        </div>
        
      </header>
    </div>
    </div>
  );
}

export default App;
