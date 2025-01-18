$(document).ready(function () {
    const $carouselContainer = $('.carousel-container');
    const $carouselItems = $('.carousel-item');
    const $prevBtn = $('.prev');
    const $nextBtn = $('.next');
  
    let currentIndex = 0;
  
    // Show initial slide
    $($carouselItems[currentIndex]).addClass('active');
  
    // Previous button click event
    $prevBtn.click(function () {
      $($carouselItems[currentIndex]).removeClass('active');
      currentIndex = (currentIndex - 1 + $carouselItems.length) % $carouselItems.length;
      $($carouselItems[currentIndex]).addClass('active');
    });
  
    // Next button click event
    $nextBtn.click(function () {
      $($carouselItems[currentIndex]).removeClass('active');
      currentIndex = (currentIndex + 1) % $carouselItems.length;
      $($carouselItems[currentIndex]).addClass('active');
    });
  });
  $(document).ready(function () {
    // Carousel
    const $carouselContainer = $('.carousel-container');
    const $carouselItems = $('.carousel-item');
    const $prevBtn = $('.prev');
    const $nextBtn = $('.next');
  
    let currentIndex = 0;
  
    // Show initial slide
    $($carouselItems[currentIndex]).addClass('active');
  
    // Previous button click event
    $prevBtn.click(function () {
      $($carouselItems[currentIndex]).removeClass('active');
      currentIndex = (currentIndex - 1 + $carouselItems.length) % $carouselItems.length;
      $($carouselItems[currentIndex]).addClass('active');
    });
  
    // Next button click event
    $nextBtn.click(function () {
      $($carouselItems[currentIndex]).removeClass('active');
      currentIndex = (currentIndex + 1) % $carouselItems.length;
      $($carouselItems[currentIndex]).addClass('active');
    });
  
    // Animation
    // No additional JavaScript needed for the provided animation.
  
    // Testimonial Carousel
    $('.testimonial-content').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 3000,
    });
  });
  $(document).ready(function() {
    // Sample course data (you can replace this with your actual data)
    var courses = [
      { title: "Entrepreneurship 101", description: "Learn the fundamentals of entrepreneurship." },
      { title: "Digital Marketing Strategies", description: "Master online marketing techniques." },
      { title: "Business Plan Development", description: "Create a comprehensive business plan." }
      // Add more courses here
    ];
  
    // Loop through the course data and create course items
    var courseList = $('.course-list');
    for (var i = 0; i < courses.length; i++) {
      var courseItem = '<div class="course-card">' +
        '<h2>' + courses[i].title + '</h2>' +
        '<p>' + courses[i].description + '</p>' +
        '</div>';
      courseList.append(courseItem);
    }
  });
  $(document).ready(function() {
    // Sample team data (you can replace this with your actual data)
    var teamMembers = [
      { name: "John Doe", role: "Founder", bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit." },
      { name: "Jane Smith", role: "CEO", bio: "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium." },
      // Add more team members here
    ];
  
    // Loop through the team data and create team member items
    var teamList = $('.team-list');
    for (var i = 0; i < teamMembers.length; i++) {
      var teamMember = '<div class="team-member">' +
        '<img src="team' + (i + 1) + '.jpg" alt="Team Member">' +
        '<h3>' + teamMembers[i].name + '</h3>' +
        '<p>' + teamMembers[i].role + '</p>' +
        '<p>' + teamMembers[i].bio + '</p>' +
        '</div>';
      teamList.append(teamMember);
    }
  });
  $(document).ready(function() {
    // Array to store posts (simulating a database)
    var posts = [];
  
    // Function to add a new post
    function addPost(name, message) {
      var postHTML =
        '<div class="community-post">' +
        '<h3>' + name + '</h3>' +
        '<p>' + message + '</p>' +
        '</div>';
  
      $('#communityPosts').prepend(postHTML);
    }
  
    // Post button click event
    $('#postButton').click(function() {
      var name = $('#name').val();
      var message = $('#message').val();
  
      if (name && message) {
        // Add post to array and display
        posts.push({ name: name, message: message });
        addPost(name, message);
  
        // Clear form fields
        $('#name').val('');
        $('#message').val('');
      }
    });
  
    // Display existing posts on page load (you can populate this from your backend)
    for (var i = 0; i < posts.length; i++) {
      addPost(posts[i].name, posts[i].message);
    }
  });
  $(document).ready(function() {
    // Sample project data (replace this with your actual data)
    var projects = [
      {
        name: "Project A",
        description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
      },
      {
        name: "Project B",
        description: "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
      },
      {
        name: "Project C",
        description: "Fusce a est nec diam aliquam convallis nec nec nulla.",
      }
    ];
  
    // Function to add a project to the list
    function addProject(name, description) {
      var projectHTML =
        '<div class="project-item">' +
        '<h3>' + name + '</h3>' +
        '<p>' + description + '</p>' +
        '</div>';
  
      $('.project-list').append(projectHTML);
    }
  
    // Display projects on page load
    for (var i = 0; i < projects.length; i++) {
      addProject(projects[i].name, projects[i].description);
    }
  });
  
          