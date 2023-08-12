document.getElementById("uploadButton").addEventListener("click", function() {
    // Simulate running a Python script and getting output
    const inputText = document.getElementById("inputBox").value;
    const outputText = simulatePythonScript(inputText);
    
    // Display the output in the outputBox
    const outputBox = document.getElementById("outputBox");
    outputBox.textContent = outputText;
});

function simulatePythonScript(input) {
    // Simulate processing the input and generating output
    return "Simulated output for input: " + input;
}
