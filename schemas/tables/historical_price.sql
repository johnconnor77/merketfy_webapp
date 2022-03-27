create table if not exists historical_price
(
    id                                  serial              not null,
    article_id                          integer             not null,
    price                               double precision    not null,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

