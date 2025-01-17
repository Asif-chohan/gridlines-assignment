# Interview Task: PowerPoint JSON to React Converter

## Background
You are given a JSON file (sample_slide.json) that represents a PowerPoint presentation (SampleSlide.pptx) in Syncfusion format. The JSON structure mirrors Syncfusion's PowerPoint object model, which includes:

- Shapes (IShape interface) - representing elements like:
  - AutoShapes
  - Text boxes
  - Pictures
  - Placeholders
- Properties for each shape including:
  - Position (Left, Top, Width, Height)
  - Formatting (Fill, LineFormat)
  - Text content (TextBody)
  - Rotation
  - Hyperlinks
  - PlaceholderFormat

Syncfusion is a document processing library that provides a comprehensive API for working with PowerPoint presentations programmatically. The JSON format we're working with represents a PowerPoint file using Syncfusion's object model and class structures.

## Task
Write Python code to convert this Syncfusion-formatted JSON into React components that can render the presentation content. The code should map Syncfusion's PowerPoint object model to appropriate React components and styles.

This is a 2-hour project - focus on demonstrating your approach and getting as much done as you can in the time available. You'll be using Cursor AI to assist with the development process.

## Evaluation Criteria
The candidate will be evaluated on their ability to:
- Write clean, efficient, and well-structured Python code
- Parse and transform the Syncfusion JSON schema correctly
- Generate valid React component code that preserves the PowerPoint elements' visual properties
- Implement proper error handling for invalid JSON or unsupported PowerPoint features
- Demonstrate understanding of both PowerPoint/Syncfusion concepts and React components
- Write maintainable and documented code
- Make effective use of Cursor AI while maintaining code quality

## Deliverables
1. Python script that performs the conversion
2. Brief documentation explaining the approach and mapping between Syncfusion and React concepts
3. Any assumptions or limitations of the implementation

## Submission
Please submit your work by:
1. Cloning this repository
2. Creating a new repository under your own GitHub account
3. Pushing your solution to your repository
4. Adding a screenshot comparison to the repo showing the rendered React component, so it's easy to compare the original PowerPoint slide to the React component render result:
   - Original PowerPoint slide (SampleSlide.pptx)
   - Your React component render result
5. Inviting https://github.com/stephaniegoldman12 as a collaborator to view your work

Good luck!