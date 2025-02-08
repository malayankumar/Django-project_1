function toggleDescription(element) {
    const desc = element.previousElementSibling || element;
  
    if (desc.classList.contains('expanded')) {
      desc.classList.remove('expanded');
      desc.style.webkitLineClamp = '2';
      desc.style.height = '3em';
      element.textContent = '... Read more';
    } else {
      desc.classList.add('expanded');
      desc.style.webkitLineClamp = 'unset';
      desc.style.height = 'auto';
      element.textContent = ' Show less';
    }
  }
  