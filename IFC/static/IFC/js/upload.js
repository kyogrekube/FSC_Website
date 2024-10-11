const createAcrHTML = ({
    id, title, body
//    <div class="acr" id="artist-${id}">
  }) => `
    <div class="acr" id="artist-${id}">
      <a class="frame-link" href="#">
        <img class="photo" src="${portrait}" alt="${name}"/>
      </a>
      <h2 class="name">${name}</h2>
      <span class="description">
        <p class="country">${country}</p>
        <p class="city">${city}</p>
        <p class="tagline">${tagline}</p>
        <p class="price">${price}</p>
      </span>
      <span class="label">
        <ul class="tags-label">
          ${tags.map(tag => `
            <li class="tag-elm">
              <a href="#" class="tag">${tag}</a>
            </li>`
          ).join('')}
        </ul>
      </span>
    </div>`;
   
  // Create the HTML for each artist.
  const artists = data.artists.map(createArtistHTML);
  
  // And add it for each HTML template to the body.
  artists.forEach(artist => {
    document.body.innerHTML += artist;
  });