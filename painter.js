    // js canvas drawing function stuff
    var canvas = document.getElementById('drawingCanvas');
    var ctx = canvas.getContext('2d');
    var isDrawing = false;
    var lastX = 0;
    var lastY = 0;
    var strokeColor = 'black';
    var lineWidth = 10; 
 
    canvas.addEventListener('mousedown', function(e) {
      isDrawing = true;
      [lastX, lastY] = [e.offsetX, e.offsetY];
    });
   
    canvas.addEventListener('mousemove', function(e) {
      if (!isDrawing) return;
      ctx.beginPath();
      ctx.moveTo(lastX, lastY);
      ctx.lineTo(e.offsetX, e.offsetY);
      ctx.strokeStyle = strokeColor;
      ctx.lineWidth = lineWidth; 
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      ctx.stroke();
      [lastX, lastY] = [e.offsetX, e.offsetY];
    });
    
    canvas.addEventListener('mouseup', function() {
      isDrawing = false;
    });
  
    canvas.addEventListener('mouseout', function() {
      isDrawing = false;
    });
    
    document.querySelectorAll('.colorSelector').forEach(item => {
      item.addEventListener('click', function() {
        strokeColor = this.style.backgroundColor;
      });
    });
    var eraserEnabled = false;
    document.getElementById('eraser').addEventListener('click', function() {
      eraserEnabled = !eraserEnabled;
      if (eraserEnabled) {
        strokeColor = 'white'; 
      } else {
        strokeColor = 'black'; 
      }
    });
    
    document.querySelectorAll('.lineWidthSelector').forEach(item => {
      item.addEventListener('click', function() {
        lineWidth = parseInt(this.textContent); 
      });
    });
    // event listener drawing choice
    var drawingChoices = document.querySelectorAll('input[name="drawingChoice"]');
    drawingChoices.forEach(function(choice) {
      choice.addEventListener('change', function() {
        var selectedChoice = document.querySelector('input[name="drawingChoice"]:checked').value;
        document.getElementById('question').textContent = "You are drawing a " + selectedChoice + ".";
        displayAnswerImage(selectedChoice);
      });
    });
    // displays answer image
    function displayAnswerImage(choice) {
      switch (choice) {
        case 'Cat':
          drawImageOnCanvas('assets/img/fill-in-cat.png');
          break;
        case 'Cookie':
          drawImageOnCanvas('assets/img/fill-in-cookie.png');
          break;
        case 'House':
          drawImageOnCanvas('assets/img/fill-in-house.png');
          break;
      }
    }
   
    function drawImageOnCanvas(imgource) {
      const img = new Image();
      img.onload = function() {
        ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      };
      img.src = imgource;
    }
    drawingChoices.forEach(function(choice) {
      choice.addEventListener('change', function() {
        var selectedChoice = document.querySelector('input[name="drawingChoice"]:checked').value;
        switch (selectedChoice) {
          case 'Cat':
            drawImageOnCanvas('assets/img/fill-in-cat.png');
            break;
          case 'Cookie':
            drawImageOnCanvas('assets/img/fill-in-cookie.png');
            break;
          case 'House':
            drawImageOnCanvas('assets/img/fill-in-house.png');
            break;
        }
      });
    });