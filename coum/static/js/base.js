function handleFileUpload(files, obj) {
	for( var i = 0; i < files.length; i++ ) {
        // ... your other code
       	var reader = new FileReader();
        reader.onload = function(){
            // Should look like data:,<jibberish_data> based on which method you called
            console.log(e.target.result);
        };
        reader.readAsDataURL(files[i]);
    }
}