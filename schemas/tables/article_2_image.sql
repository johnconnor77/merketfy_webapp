create table if not exists article_2_image
(
    id                                  serial              not null,
    article_id                          integer             not null,
    image_id                            integer             not null,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

