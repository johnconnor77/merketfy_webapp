create table if not exists person_2_favourite
(
    id                                  serial              not null,
    person_id                           integer             not null,
    favourite_id                        integer             not null,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

