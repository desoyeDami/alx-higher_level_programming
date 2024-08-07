$.get('https://swapi-api.alx-tools.com/api/films/?format=json')
    .done(function(data) {
        const films = data.results;
        const $list = $('#list_movies');
        $list.empty();
        films.forEach(film => {
            $list.append(`<li>${film.title}</li>`);
        });
    })
