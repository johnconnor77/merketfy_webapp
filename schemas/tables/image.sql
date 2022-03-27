create table if not exists image
(
    id                                  serial              not null,
    name                                varchar(128)        not null,
    url                                 varchar             not null,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

