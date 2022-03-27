create table if not exists user_2_alert
(
    id                                  serial              not null,
    user_id                             integer             not null,
    alert_id                            integer             not null,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

