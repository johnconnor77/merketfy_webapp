create table if not exists alert
(
    id                                  serial              not null,
    article_id                          integer             not null,
    target_price                        double precision    not null,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

