"
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title}Image Cropping{/title>
    <style>
        .image-container {
        width: 458px; /* Width of the container */
        height: 140px; /* Height of the container */
        overflow: hidden; /* Hide parts of the image that don't fit */
        border-radius: 15px; /* Rounded corners */
        position: relative; /* Relative positioning for the child element */
    }

    .image {
        object-fit: cover; /* Cover the entire container */
        object-position: center; /* Center the image */
        width: 100%; /* Full width */
        height: 100%; /* Full height */
    }
   </style>
</head>
<body>
    <div class='image-container'>
        <img src='"&x&"' alt='Album Cover' class='image'>
    </div>
</body>
</html>
"
