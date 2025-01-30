import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
  const [image, setImage] = useState(null);

  const handleImageUpload = (event) => {
    setImage(event.target.files[0]);
  };

  const submitImage = () => {
    const formData = new FormData();
    formData.append('image', image);
    axios.post('/api/image/upload', formData)
      .then(response => {
        alert(response.data.message);
      })
      .catch(error => {
        alert('Image upload failed');
      });
  };

  return (
    <div>
      <h1>Upload Image</h1>
      <input type="file" onChange={handleImageUpload} />
      <button onClick={submitImage}>Upload</button>
    </div>
  );
}

export default ImageUpload;
